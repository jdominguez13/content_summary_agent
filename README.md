# content_summary_agent
Repository for all content summary agents:

* AI Content


AI agent for scraping, summarizing, and delivering news/blog content with feedback loop and Snowflake/Streamlit integration.

## Project Structure

```
content_summary_agent/
├── data_pipeline/         # Scripts for scraping, summarizing, storing, and emailing
│   ├── __init__.py
│   ├── fetch_articles.py  # Scrape or fetch news/articles
│   ├── summarize.py       # Summarize articles
│   ├── store_snowflake.py # Store data in Snowflake
│   ├── emailer.py         # Email delivery
│   └── main.py            # Orchestrates the pipeline
├── feedback_app/          # Streamlit app for feedback
│   ├── __init__.py
│   └── app.py
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
└── README.md
```

## Features
- Scrape and summarize news/blogs about AI productivity and revenue
- Store content and feedback in Snowflake
- Generate daily blog post
- Email delivery of summaries and blog post
- Streamlit feedback app for relevancy ranking
- Personalization based on feedback

## Quick Start
1. Clone the repo
2. Set up your environment variables (see `.env.example`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the data pipeline: `python data_pipeline/main.py`
5. Launch feedback app: `streamlit run feedback_app/app.py`

# Snowflake configuration
SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
SNOWFLAKE_ROLE: ${{ secrets.SNOWFLAKE_ROLE }}
SNOWFLAKE_WAREHOUSE: ${{ secrets.SNOWFLAKE_WAREHOUSE }}
SNOWFLAKE_DATABASE: ${{ secrets.SNOWFLAKE_DATABASE }}
SNOWFLAKE_SCHEMA: ${{ secrets.SNOWFLAKE_SCHEMA }}

# Email configuration
EMAIL_HOST: ${{ secrets.EMAIL_HOST }}
EMAIL_PORT: ${{ secrets.EMAIL_PORT }}
EMAIL_USER: ${{ secrets.EMAIL_USER }}
EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}
EMAIL_TO: ${{ secrets.EMAIL_TO }}

# News API
NEWS_API_KEY=your_news_api_key
