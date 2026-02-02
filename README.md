# AI Content Recommendation Agent (Marketing & AdTech)
A lightweight AI-powered content recommendation system that personalizes marketing content based on user interests.
## What it does
- Collects user interests via Google Forms (stored in Google Sheets)
- Stores content metadata in Airtable
- Converts content + user interests into embeddings
- Ranks content using cosine similarity
- Returns top 3 recommended items with links
## Why it matters (Marketing & AdTech)
This project demonstrates personalization — a core capability for:
- campaign optimization
- customer engagement
- content strategy
- ad targeting & segmentation
## Tech Stack
- OpenAI Embeddings (`text-embedding-3-small`)
- Python, Pandas, NumPy
- Scikit-learn (cosine similarity)
- Airtable (content database)
- Google Forms/Sheets (user interest collection)
## Demo Screenshots
See `/images`:
- Airtable content table
- Google Form + Sheets response
- Recommendation output
## Run locally
1) Install dependencies:
```bash
pip install -r requirements.txt
