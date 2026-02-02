import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

MODEL = "text-embedding-3-small"

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY. Set it in your environment.")
    return OpenAI(api_key=api_key)

def get_embedding(client, text: str):
    text = str(text).strip()
    resp = client.embeddings.create(model=MODEL, input=text)
    return resp.data[0].embedding

def find_topic_column(user_df: pd.DataFrame) -> str:
    # Try to auto-detect the topics column
    candidates = [c for c in user_df.columns if "topic" in c.lower() or "interested" in c.lower()]
    if not candidates:
        raise KeyError(f"Could not find a topics column. Columns: {list(user_df.columns)}")
    return candidates[0]

def main():
    content_path = "data/sample_content_library.csv"
    user_path = "data/sample_user_preferences.csv"

    content_df = pd.read_csv(content_path)
    user_df = pd.read_csv(user_path)

    client = get_client()

    # Build content embeddings
    content_df["embedding"] = content_df["Description"].apply(lambda x: get_embedding(client, x))

    # User interest
    topic_col = find_topic_column(user_df)
    user_interest = str(user_df.iloc[0][topic_col])
    user_embedding = get_embedding(client, user_interest)

    # Similarity + top 3
    content_embeddings = np.vstack(content_df["embedding"].values)
    sims = cosine_similarity([user_embedding], content_embeddings)[0]
    content_df["similarity"] = sims

    top = content_df.sort_values("similarity", ascending=False).head(3)
    print("\nTop Recommendations:")
    print(top[["Title", "URL", "similarity"]].to_string(index=False))

if __name__ == "__main__":
    main()
