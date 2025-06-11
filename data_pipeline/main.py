import os
import sys

if os.getenv("GITHUB_ACTIONS") != "true":
    print("This script is intended to be run only in GitHub Actions CI/CD.")
    sys.exit(1)

# from dotenv import load_dotenv
from fetch_articles import fetch_articles
from summarize import summarize_article
from store_snowflake import store_articles
from emailer import send_email


# load_dotenv()

def generate_blog_post(summaries):
    # Simple blog post generator
    blog = "<h2>Daily AI Rundown</h2>\n<ul>"
    for s in summaries:
        blog += f"<li><b>{s['title']}</b>: {s['summary']}<br><a href='{s['url']}'>Read more</a></li>"
    blog += "</ul>"
    return blog

def main():
    print("Fetching articles...")
    articles = fetch_articles()
    print(f"Fetched {len(articles)} articles.")
    for article in articles:
        print(f"Summarizing: {article['title']}")
        article['summary'] = summarize_article(article['content'] or article['description'])
    # store_articles(articles)  # Removed for this workflow
    blog_post = generate_blog_post(articles)
    send_email(
        subject="Daily AI Rundown",
        body=blog_post
    )
    print("Done.")

if __name__ == '__main__':
    main() 