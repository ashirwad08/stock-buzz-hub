import requests
from requests_oauthlib import OAuth1
from os.path import expanduser
import cnfg
import pandas as pd
import numpy as np
import tweepy

home = expanduser('~')
twitterConfigFile = '/.twitter_config'


def connect_twitter(config=cnfg.load(home + twitterConfigFile)):
    """
    load twitter app configs and return api object
    """
    try:
        auth = tweepy.OAuthHandler(config['consumer_key'], 
                                   config['consumer_secret'])
        auth.set_access_token(config['access_token'],
                              config['access_token_secret'])
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError as e:
        print e.message[0]['code']
        print e.args[0][0]['code']
        
        
def get_tweets(api, query):
    """
    Hit twitter api with query string
    (future: build on query parameters)
    
    Returns large dataframe of tweets and attributes
    """
    
    results = []
    for tweet in tweepy.Cursor(api.search, q=query).items(1000):
        results.append(tweet)
    
    id_list = [tweet.id for tweet in results]
    #unpack into dataframe
    data = pd.DataFrame(id_list,columns=['id'])
    
    data["text"]= [tweet.text.encode('utf-8') for tweet in results]
    data["datetime"]=[tweet.created_at for tweet in results]
    data["Location"]=[tweet.place for tweet in results]
    
    return data

