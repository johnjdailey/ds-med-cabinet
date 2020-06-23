# Recommend.py

# Strain recommend function using k nearest neighbors and tfidf vectorizer train on strain Effects.


# Imports

from os import path
import pandas as pd
import pickle
import json


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "../DS_Med_Cabinet/data/Leafly.csv")

df = pd.read_csv(file_name)


# Import pickled model

model_path = path.join(path.dirname(__file__), "../DS_Med_Cabinet/pickles/nn.pkl")

NN_model = pickle.load(open(model_path, 'rb'))


# Import pickled vectorizer

vectorizer_path = path.join(path.dirname(__file__), "../DS_Med_Cabinet/pickles/tfidf.pkl")

tfidf = pickle.load(open(vectorizer_path, 'rb'))


# Recommend function

def recommend(user_input):
    temp_df = NN_model.kneighbors(tfidf.transform([user_input]).todense())[1]
    

    #print(temp_df)
    
    for i in range(4):
        info_strain = df.loc[temp_df[0][i]]['Strain']
        info_type = df.loc[temp_df[0][i]]['Type']
        info_rating = df.loc[temp_df[0][i]]['Rating']
        info_effects = df.loc[temp_df[0][i]]['Effects']
        info_flavor = df.loc[temp_df[0][i]]['Flavor']
        info_description = df.loc[temp_df[0][i]]['Description']
    
        strain = json.dumps(info_strain)
        typ = json.dumps(info_type)
        rating = json.dumps(info_rating)
        effects = json.dumps(info_effects)
        flavor = json.dumps(info_flavor)
        description = json.dumps(info_description)

        #print(strain)
        #print(typ)
        #print(rating)
        #print(effects)
        #print(flavor)
        #print(description)
        #print(strain, typ, rating, effects, flavor, description)

        return strain
        #return type
        #return rating
        #return effects
        #return flavor
        #return description

        #return strain
        
        #return strain + typ + rating + effects + flavor + description


recommend("Happy,Relaxed,Uplifted,Focused,Aroused")
