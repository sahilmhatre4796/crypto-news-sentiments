import requests

def get_crypto_news():
    url = "https://newsapi.org/v2/everything?q=crypto&sortBy=publishedAt&language=en&apiKey=6699232a886c4b51b4d79e4554970be1"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])
