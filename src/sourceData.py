import requests
from requests_oauthlib import OAuth1
from os.path import expanduser
import cnfg
import pandas as pd
import numpy as np
import tweepy
import json
from pymongo import MongoClient

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
    NOT IMPLEMENTED: Check Cache for tweet document, if not available then
    query MongoDB, if query string not in DB index, then fetch from twitter.
    
    
    Hit twitter api with query string
    (future: build on query parameters)
    
    Returns large dataframe of tweets and attributes
    """
    
    results = []
    for tweet in tweepy.Cursor(api.search, q=query).items(1000):
        results.append(tweet)
    
    return results, query
    
    
    
def write2db(data, query):
    """
    takes in a list of json tweet events and writes to a MongoDB. 
    Every document is a tweet
    event. Document 'symbol' should id the stock symbol. 'query_string' should 
    store the query string used to fetch the symbol for quick cache retrieval
    later on.
    """
    
    
    client = MongoClient()
    db = client.tweet_stream
    tweets = db.tweets
    
    for tweet in data:
        data={}
        #write to db with corresponding query so it can be cached later
        data['query']=query 
        data['tweet']=tweet.text.encode('utf-8')
        data['datetime']=tweet.created_at
        tweets.insert_one(data)



def write2cache(data):
    """
    writes a document to Redis Cache if queried for first time. 
    """  
    

def load_from_cache():
    """
    Loads document from cache if query string availabel in cache index
    """  
    
    
def read_from_db(#HOW DO WE READ FROM MONGODB???):
    """
    If query string not in cache index then check if query string in MongoDB
    index. If not, return control to fetch from API.
    """
    id_list = [tweet.id for tweet in results]
    ##unpack into dataframe
    data = pd.DataFrame(id_list,columns=['id'])
    
    #data["text"]= [tweet.text.encode('utf-8') for tweet in results]
    #data["datetime"]=[tweet.created_at for tweet in results]
    #data["Location"]=[tweet.place for tweet in results]
    
    
    
    
    
    

