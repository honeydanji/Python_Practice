import tweepy
import pandas as pd
from Twitter_Crolling import setting

# 트위터에 인증
auth = tweepy.OAuthHandler(setting.consumer_key, setting.consumer_secret)
auth.set_access_token(setting.access_token, setting.access_token_secret)

# API Client 생성
api = tweepy.API(auth, wait_on_rate_limit=True)

# 데이터를 저장할 데이터프레임 생성
df = pd.DataFrame(columns=['user', 'date', 'text'])

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global df
        df = df.append({"date": status.created_at, "user": status.user.screen_name, "text": status.text}, ignore_index=True)

    def on_error(self, status_code):
        if status_code == 420:
            # 트위터의 요청 제한에 도달했을 경우 연결을 끊습니다.
            return False
# 해시태그 목록 정의
lst_hashtags = ["it", "informationtechnology", "tech", "software", "programming"]

# 스트림을 시작합니다.
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=lst_hashtags)

# 데이터프레임을 CSV 파일로 저장합니다.
df.to_csv('tweets.csv', index=False)

df = pd.read_csv('tweets.csv')
print(df.head())
