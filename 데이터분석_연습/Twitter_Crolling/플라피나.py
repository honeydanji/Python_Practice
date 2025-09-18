from pathlib import Path
import os
import twitter, time
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경 변수를 셸 환경 변수로 로드

# twitter API
twitter_consumer_key = os.getenv("TWITTER_key")
twitter_consumer_secret = os.getenv("TWITTER_secret_key")
twitter_access_token = os.getenv("TWITTER_access_token")
twitter_access_secret = os.getenv("TWITTER_access_token_secret")

twitter_api = twitter.Api(
    consumer_key=twitter_consumer_key,
    consumer_secret=twitter_consumer_secret,
    access_token_key=twitter_access_token,
    access_token_secret=twitter_access_secret,
)

# 특정 계정의 타임라인 긁어오기
account = "plafina"
timeline = twitter_api.GetUserTimeline(
    screen_name=account, count=20, include_rts=True, exclude_replies=False
)
# 해당 계정의 최근 트윗 200개를 가져온다.

for tweet in timeline:
    print(tweet)
