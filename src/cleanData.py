
import pandas as pd
import numpy as np

def clean_twitter_data(data):
    """
    Takes in a dataframe of tweets and performs the following operations:
    1. encode to UTF-8
    2. strip superflous characters but save emoticons :) :( :D :-) :-(
    2.1 preserve hashtags (treat as distinct vocabulary elements)
    2.2 nice to have feature: extract any numbers indicating stock price
        and add to sentiment score if price is above below current stock price.
        (captures profit targets or entry points; bullish/bearish)
    2.3 remove links
    2.4 lowercase
    2.5 strip out query string elements from tweet
    3. remove stopwords selectively
    6. stem
    7. lemmatize (plurals, symbols and words, ...)
    """
    
    #xxxxxxxxxxxxxxxxxxxxxxxx REGEX-FU xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #-------------
    #normalize unicode encoding to remove accents, etc.
    #-------------
    """
    if strings are transformed into their normalized forms, then canonical-equivalent ones will also have precisely the same binary representation. The Unicode Standard provides well-defined normalization forms that can be used for this: NFC and NFD.

For loose matching, programs may want to use the normalization forms NFKC and NFKD, which remove compatibility distinctions. 
    """
    data['text']=data['text'].map(lambda val: uc.normalize('NFKD',unicode(val,'utf-8')))
    
    #-------------
    #preserve words (remove digits for now), strip other symbols,links EXCEPT
    ## 
    ## hashtags
    ## emoticons :), :(, :D, :-), :-(
    #-------------
    data.text.replace({'http.+\s':''},regex=True)
    data.text.replace({'[^A-Za-z#]':' '}, regex=True, inplace=True)
    data.text.replace({'\s+':' '}, regex=True, inplace=True)
    data.text.replace({'\s.\s':' '}, regex=True, inplace=True)
    data['text']=data.text.map(lambda val: val.lower())
    #todo: strip Emoticons!
    #strip out query parameters (e.g. aapl, #aapl, apple, etc.)
    #note: make sure dataframe has query parameters as a field from the original
    #query... something like....
    data.text.replace({'apple|#aapl|#apple|aapl':''}, regex=True)
    
    
   #-------------
   #remove duplicate rows
   #-------------
   data.drop_duplicates(subset='text', keep='first',inplace=True)
   
   #-------------
   #remove stopwords
   #-------------
   
   
   #-------------
   #stem words
   #-------------
   
   
   #-------------
   #lemmatize
   #-------------
   
   



   
   

    

