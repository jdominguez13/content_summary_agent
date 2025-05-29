import streamlit as st
import snowflake.connector
import os
import pandas as pd
from datetime import datetime

# Snowflake connection
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

def fetch_articles():
    conn = get_connection()
    df = pd.read_sql("SELECT ID, TITLE, URL, SUMMARY, PUBLISHED_AT FROM ARTICLES ORDER BY PUBLISHED_AT DESC LIMIT 20", conn)
    conn.close()
    return df

def store_feedback(article_id, score, comment):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS FEEDBACK (
            ID INTEGER AUTOINCREMENT,
            ARTICLE_ID INTEGER,
            SCORE INTEGER,
            COMMENT STRING,
            TIMESTAMP TIMESTAMP
        )
    """)
    cur.execute(
        "INSERT INTO FEEDBACK (ARTICLE_ID, SCORE, COMMENT, TIMESTAMP) VALUES (%s, %s, %s, %s)",
        (article_id, score, comment, datetime.utcnow())
    )
    conn.commit()
    cur.close()
    conn.close()

st.title("AI News Feedback")

articles = fetch_articles()
for idx, row in articles.iterrows():
    st.subheader(row['TITLE'])
    st.write(row['SUMMARY'])
    st.markdown(f"[Read more]({row['URL']})")
    with st.form(key=f"feedback_{row['ID']}"):
        score = st.slider('Relevancy (1=Not relevant, 5=Highly relevant)', 1, 5, 3)
        comment = st.text_input('Comments (optional)')
        submitted = st.form_submit_button('Submit Feedback')
        if submitted:
            store_feedback(row['ID'], score, comment)
            st.success('Feedback submitted!') 