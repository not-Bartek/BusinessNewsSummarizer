from dotenv import load_dotenv
import os
import requests
import feedparser
from bs4 import BeautifulSoup

load_dotenv()
api_key = os.environ.get("NEWSAPI_KEY")

link='https://www.bbc.com/news/articles/cy59kxl2xwzo'
lang='en'
category='business'
articleCount=1
url = f"https://newsapi.org/v2/top-headlines?category={category}&language={lang}&pageSize={articleCount}&apiKey={api_key}"
#response = requests.get(url)
#data = response.json()

# for article in data.get("articles", []):
#     print(article.get("title"))
#     print(article.get("url"))
#     print("---")

# response2 = requests.get(link)
# soup = BeautifulSoup(response2.text, "html.parser")

# paragraphs = soup.find_all("p")
# full_text = " ".join([p.get_text() for p in paragraphs])
# print(full_text)

rss_url = "http://feeds.bbci.co.uk/news/business/rss.xml"
feed = feedparser.parse(rss_url)
print(feed.entries[1])

for entry in feed.entries:
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("Description:", entry.summary)
    print("Date:", entry.published)
    print("---")