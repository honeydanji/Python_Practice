from requests.models import PreparedRequest
import os
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv

load_dotenv()

# twitter API
twitter_consumer_key = os.getenv("TWITTER_key")
twitter_consumer_secret = os.getenv("TWITTER_secret_key")
twitter_access_token = os.getenv("TWITTER_access_token")
twitter_access_secret = os.getenv("TWITTER_access_token_secret")


twitter = OAuth1Session(
    twitter_consumer_key,
    client_secret=twitter_consumer_secret,
    resource_owner_key=twitter_access_token,
    resource_owner_secret=twitter_access_secret,
)

url = "https://api.twitter.com/2/tweets/search/recent"
query = "from:plafina"

params = {"query": query, "tweet.fields": "created_at"}

response = twitter.get(url, params=params)

if response.status_code != 200:
    raise Exception(
        f"Request returned an error: {response.status_code}, {response.text}"
    )

tweets = response.json()

for tweet in tweets["data"]:
    print(tweet)
