import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.itworld.co.kr/main/"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the news articles on the page
news_articles = soup.find_all("div", class_="news_list_area")

# Extract the information from the news articles
for article in news_articles:
    title = article.find("h4").text.strip()
    date = article.find("span", class_="date").text.strip()
    link = article.find("a")["href"]
    print(f"Title: {title}\nDate: {date}\nLink: {link}\n")
