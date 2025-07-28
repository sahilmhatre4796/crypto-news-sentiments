import streamlit as st
from news_aggregator import get_crypto_news
from sentiment_analyzer import analyze_sentiment

st.set_page_config(page_title="Crypto News & Sentiment Tool", layout="wide")
st.title("📰 Crypto News & Sentiment Tool")

articles = get_crypto_news()

for article in articles:
    title = article.get("title", "No Title")
    desc = article.get("description", "")
    url = article.get("url", "#")
    sentiment = analyze_sentiment(f"{title} {desc}")

    st.subheader(title)
    st.write(desc)
    st.markdown(f"**Sentiment:** {sentiment}")
    st.markdown(f"[Read more]({url})")
    st.markdown("---")
