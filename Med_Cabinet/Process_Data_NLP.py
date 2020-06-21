# Process_Data_NLP.py



# Imports

import pandas as pd
import re
import string
import matplotlib.pyplot as plt
import numpy as np
import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


"""Data Exploration and Cleaning"""


file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly.csv"


# Import CSV

df = pd.read_csv(file_name)


# Explore df shape

#print(df.shape)
# 2351 rows × 6 columns
#df


# Check Effects column for null values as its being used as a predictor

#df['Effects'].isnull().sum()
# 0


# Check Description column for nulls values and count

#df['Description'].isnull().value_counts()
#False    2318
#True       33
#Name: Description, dtype: int64


# Show Description column rows with null values

#df[df['Description'].isnull()]


# Dropping the rows with null values

df = df.dropna()


# Verifying change in rows

#len(df['Description'])
# 2277


# Check data type of Description column

#df["Description"].dtype
# dtype('O')


# Consider replacing . with , in Description column

#df['Description'] = df['Description'].apply(str).str.replace('.', ',')


# Example of Effects column in the first row

#df["Effects"][0]
# 'Creative,Energetic,Tingly,Euphoric,Relaxed'


""" Machine Learning """


# Imports

import spacy
from spacy.tokenizer import Tokenizer
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer


# Instantiate nlp with pretrained statistical model for English language (first install with, "python -m spacy download en_core_web_lg")

nlp = spacy.load("en_core_web_lg")
df.head()


# The Tokenizer

tokenizer = Tokenizer(nlp.vocab)


# Make the tokens for descrption

description_tokens = []
for txt in tokenizer.pipe(df['Description'], batch_size=500):
    txt_tokens = [token.text for token in txt]
    description_tokens.append(txt_tokens)
df['description_tokens'] = description_tokens
#print(df['description_tokens'].head())


# Make the tokens for flavor

flavor_tokens = []
for txt in tokenizer.pipe(df['Flavor'], batch_size=500):
    txt_tokens = [token.text for token in txt]
    flavor_tokens.append(txt_tokens)
df['flavor_tokens'] = flavor_tokens
#print(df['flavor_tokens'].head())


#  Make the tokens for effects

effects_tokens = []
for txt in tokenizer.pipe(df['Effects'], batch_size=500):
    txt_tokens = [token.text for token in txt]
    effects_tokens.append(txt_tokens)
df['effects_tokens'] = effects_tokens
#print(df['effects_tokens'].head())


# Make the combined column for description, flavor and effects tokens (ValueError: Length of values does not match length of index)

#df['combined_tokens'] = description_tokens + flavor_tokens + effects_tokens

#print(df['combined'] = description_tokens + flavor_tokens + effects_tokens)
# 0    [$100, OG, is, a, 50/50, hybrid, strain, that,...
# 1    [The, ‘98, Aloha, White, Widow, is, an, especi...
# 2    [1024, is, a, sativa-dominant, hybrid, bred, i...
# 3    [13, Dawgs, is, a, hybrid, of, G13, and, Chemd...
# 4    [Also, known, as, Kosher, Tangie,, 24k, Gold, ...
# Name: description_tokens, dtype: object
# /Users/amybeisel/opt/anaconda3/envs/U4-S1-NLP/lib/python3.7/site-packages/ipykernel_launcher.py:17: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy


# Check df
#df.head()


# Tokenize function on document

def tokenize(document):
    
    doc = nlp(document)
    
    return [token.lemma_.strip() for token in doc if (token.is_stop != True) and (token.is_punct != True)]


# Instantiate vectorizer object

tfidf = TfidfVectorizer(stop_words = 'english',
                       #ngram_range = (1,2),
                       max_features = 5000)


# Create a vocabulary and tf-idf score per document

dtm = tfidf.fit_transform(df['Description'])
                         

# Get feature names to use as dataframe column headers

dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
nn = NearestNeighbors(n_neighbors=4, algorithm='kd_tree')
var = nn.fit(dtm)


# View Feature Matrix as DataFrame

#print(dtm.shape)
#dtm.head()


# Query Using kneighbors 

#nn.kneighbors([dtm.iloc[0]])
# (array([[0., 1., 1., 1.]]), array([[   0, 1607, 1605, 1606]]))


#df['Description'][0][:150]
# '$100 OG is a 50/50 hybrid strain that packs a strong punch. The name supposedly refers to both its strength and high price when it first started showi'


#df['Description'][338][:150]
#'A hybrid cross of Blueberry and Haze, provides a sweet smoke and pleasant high. \xa0Pace yourself with this one, overdoing it can send you to dreamland.\xa0'


# Instantiate ideal with the hypothetical ideal Effects for a Strain to be predicted

#ideal = ["""
#Creative,Uplifted,Tingly,Euphoric,Relaxed, Giggly
#"""]


# Query the ideal Strain

#new = tfidf.transform(ideal)
#new
# <1x5000 sparse matrix of type '<class 'numpy.float64'>'
	# with 6 stored elements in Compressed Sparse Row format>


# NearestNeighbors predicts row 1605 as the best Strain considering the ideal input, as well as 1606, 1698, and 1607

#nn.kneighbors(new.todense())
# (array([[1., 1., 1., 1.]]), array([[1605, 1606, 1698, 1607]]))


# (Most) Ideal Strain Description

#df['Description'][1605]
#'Pineapple Super Silver Haze from Fire Bros. is a sativa strain that modifies the widely cherished Super Silver Haze with a Pineapple hybrid strain. 
# This second parent is thought to be either Pineapple Express or Pineapple, a phenotype of Ed Rosenthal Super Bud. The Haze genetics in this strain 
# come through in both flavor and effect, as Pineapple Super Silver Haze delivers a high-flying cerebral buzz alongside a spicy, zesty flavor. 
# Its aroma is more of a tropical medley of candied mango, pineapple, and oranges. Like a cup of coffee, this sativa is a perfect pick-me-up with 
# motivating, talkative, and creative effects and minimal heaviness in the body.'


# (Most) Ideal Strain

#df['Strain'][1605]
# 'Pineapple-Super-Silver-Haze'


# (Most) Ideal Strain Effects
#df['Effects'][1605]
# 'Happy,Euphoric,Energetic,Focused,Tingly'


# Export df to csv with tokenized columns for use in Flask_API predictions

#df.to_csv('Leafly_tokenized.csv')


""" Model to be pickled, then consider importing nnPickle, dtm, and tfidf to Flask_API for making predictions there. """


import pickle


nn.fit(dtm)


# Its important to use binary mode

nnPickle = open('nnpickle_file', 'wb')

# Source, Destination 

pickle.dump(nn, nnPickle)


# Load the model from disk

#loaded_model = pickle.load(open('nnpickle_file', 'rb'))
#result = loaded_model.predict(X_test)


# Try importing this function from Flask_API module to load the pickled model

def load_model():
    with open('nnpickle_file', 'rb') as model_file:
        saved_model = pickle.load(model_file)
        return saved_model 


# Got a NotFittedError: sklearn.exceptions.NotFittedError: The TF-IDF vectorizer is not fitted in Flask_API, so try making vectorizer pickle

with open('vectorizer.pk', 'wb') as fin:
        pickle.dump(tfidf, fin)


def load_vectorizer():
    with open('vectorizer.pk', 'rb') as vectorizer_file:
        saved_vectorizer = pickle.load(vectorizer_file)
        return saved_vectorizer
