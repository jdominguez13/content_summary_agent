import snowflake.connector
import os

SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')

def get_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )

def store_articles(articles):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"USE SCHEMA {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ARTICLES (
            ID INTEGER AUTOINCREMENT,
            TITLE STRING,
            URL STRING,
            PUBLISHED_AT STRING,
            SUMMARY STRING,
            RAW_CONTENT STRING
        )
    """)
    for article in articles:
        cur.execute(
            "INSERT INTO ARTICLES (TITLE, URL, PUBLISHED_AT, SUMMARY, RAW_CONTENT) VALUES (%s, %s, %s, %s, %s)",
            (article['title'], article['url'], article['publishedAt'], article['summary'], article['content'])
        )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    # Example usage
    store_articles([
        {'title': 'Test', 'url': 'http://example.com', 'publishedAt': '2025-05-29', 'summary': 'Summary', 'content': 'Full content'}
    ]) 