import tweepy
import random
from nltk.corpus import wordnet as wn
import time

tweet_now = True;
def get_api():
	import credentials
	consumer_key = credentials.CONSUMER_KEY
	consumer_secret = credentials.CONSUMER_SECRET
	access_token = credentials.ACCESS_TOKEN
	access_secret = credentials.ACCESS_TOKEN_SECRET

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	return api

def tweet_it(api):
	print("Time: {}, tweeting".format(time.ctime()))
	mytweet = make_tweet(getnoun())
	print(mytweet)
	api.update_status(mytweet)

def getnoun():
    nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    return random.sample(nouns,1)

def make_tweet(noun):
    raw_noun = noun[0]
    out_noun = raw_noun.replace('_',' ')
    return out_noun + ' is a prison'
