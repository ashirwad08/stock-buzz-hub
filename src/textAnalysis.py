import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


def generate_tfm(data, use_idf=False, ngram_range=(1,2):
    """
    Takes in a Series of cleaned text documents, and returns a large 
    Term Frequency Matrix. 
    The SVD method treats each tweet as a document and generates a TFM with or 
    without tfidf as specifed in the parameter.
    """  
    
    
    vectorizer = TfidfVectorizer(use_idf=use_idf, ngram_range=ngram_range, stop_words=['the','it','as','a','s','inc',
                                        'RT','its','llc','at','by','with'])
    X = vectorizer.fit_transform(data)
    
    return X


def get_concepts(X, n_components):
    """
    Takes in a (possibly sparse) Term Frequency Matrix and returns the top
    components (dataframe) that result from a Singular Value Decomposition of 
    this matrix. (Latent Semantic Analysis)
    These components capture the main "concepts" across the entire corpus.
    """
    
    lsa = TruncatedSVD(n_components=n_components, n_iter=100)
    lsa.fit(X)
    
    #REVIEW THIS PART BY RUNNING IN NOTEBOOK
    terms = vectorizer.get_feature_names()
    
    concept_df = pd.DataFrame(columns=['component','term','LSAscore'])
    for i, comp in enumerate(lsa.components_):
        termsInComp = zip(np.repeat([i],len(comp)),terms,comp)
        concept_df = pd.concat([concept_df, pd.DataFrame(sorted(termsInComp, key=lambda x: x[2], reverse=True), columns=['component','term','LSAscore'])], axis=0))
    
    
    return concept_df
    
    
    
    
def get_sentiment(comp):
   """
   Takes in a series containing words and return a sentiment score for each (series)
   """  

   from textblob import TextBlob
   return comp.map(lambda text: TextBlob(text).sentiment)

    
