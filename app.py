import tweepy

import config as cfg


BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuthHandler(consumer_key=cfg.CONSUMER_KEY,
                           consumer_secret=cfg.CONSUMER_SECRET,
                           access_token=cfg.ACCESS_TOKEN,
                           access_token_secret=cfg.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)