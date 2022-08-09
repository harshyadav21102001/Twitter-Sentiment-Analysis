import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

consumer_key = "ucv4GW3XgJriTyWADc2HHmDb1"
consumer_sec = "qlmNfnIkimYWwaYCqkzv0wzJpTxEL8hxzH7zowHZQIFpQD3zTP"
access_token = "1404667409143721985-sBVGpPhZQGUI8vI1w2opOZHEAdh6Rq"
access_token_sec = "6DRHEMkTmRywLIT8b6Oe3rLkEla0mRfcKmItWyCDUtPO8"

auth = tweepy.OAuthHandler(consumer_key,consumer_sec)

auth.set_access_token(access_token,access_token_sec)

api_connect = tweepy.API(auth)

tweet_data = api_connect.search('graphic era',count=5)

for tweet in tweet_data:
  print(tweet.text)

  pos=0
  neg=0
  neu=0

  for tweet in tweet_data:
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment.polarity > 0:
       print("positive")
       pos=pos+1
    elif analysis.sentiment.polarity == 0:
       print("neutral")
       neu=neu+1
    else:
       print("negative")
       neg=neg+1

plt.xlabel("tags")
plt.ylabel("polarity")
plt.pie([pos,neg,neu],labels = ['pos','neg','neu'],autopct="%1.1f%%")