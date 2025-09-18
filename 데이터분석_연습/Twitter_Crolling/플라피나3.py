import tweepy

consumer_key = "36J2AYWC73WJJCIDnk8M9m7Vh"
consumer_secret = "OLrE0z3RHm1CHoMlybd1ZgjG0OBbGuRZLFcRy3KV964hzwBZhF"
access_token = "1511658463734099968-goRbLImMo4AgbcbKZ3siftHBx0AUcE"
access_token_secret = "UJyBUxtH6SatgOoQk8EmiUL9ctIGsnbs9yc5xSl833Guv"

client = tweepy.Client(consumer_key, consumer_secret, access_token, access_token_secret)

public_tweets = client.get_users_tweets("palfina")

for tweet in public_tweets.data:
    print(tweet.text)
