# test_Model_Flask_API.py

# This is the test site of the pickled MODEL to be used in test_Flask_API, there is no complete API here, just a mock skeleton of the test version



#Imports

import pandas as pd
import requests
from flask import Flask, json, request, jsonify
from flask_restful import Api
import pickle
from Process_Data_NLP import load_model, load_vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression # for example, but would need to embed data
from sklearn.ensemble import RandomForestClassifier # consider using if no neural net pickle model
import pdb


# Flask API

app = Flask(__name__)
api = Api(app)


# Import Leafly csv

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly_tokenized.csv"

df = pd.read_csv(file_name)

strains = df['Strain']


# Import pickled model

model_path = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\pickles\nnpickle_file"

model = pickle.load(open(model_path, 'rb'))
#model = pickle.load(open('nnpickle_file', 'rb'))
#model = load_model()


# Import pickled vectorizer

vectorizer_path = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\pickles\vectorizer.pk"

tfidf = pickle.load(open(vectorizer_path, 'rb'))

#tfidf = TfidfVectorizer(stop_words = 'english',  # NotFittedError sklearn.exceptions.NotFittedError: The TF-IDF vectorizer is not fitted
#                       #ngram_range = (1,2),
#                       max_features = 5000)


ideal = ["""
Creative,Uplifted,Tingly,Euphoric,Relaxed, Giggly
"""]

new = tfidf.transform(ideal)
#print(new)
#new

results = model.kneighbors(new.todense())
print(results)


@app.route('/predict', methods=['GET', 'POST'])
def get_predict_post():

    #print("Med Cabinet Recommendations")

    if request.method=='GET':
        
        # Request .json from Web

        get_data = request.json
        
        # Extracting first name, last name, and effects of the first matching
    
        #first_name = get_data["First Name"]
        #last_name = get_data["Last Name"]
        #effects = get_data["Effects"]
    
        # Instantiate Classifier, fit the model, make predictions, and return results ie:

        #classifier = LogisticRegression()
        #classifier.fit(effects, strains)
        #results = classifier.predict(strains)

        #results = model.predict(strains)

    #print(results)
    #return results
    