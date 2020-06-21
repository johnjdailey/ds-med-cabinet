# app_API.py

# NOT WORKING CODE, MOCKUP, NEEDS WORK, see test_Flask_API.py for functioning test


#Imports

import pandas as pd
import requests
from flask import Flask, json, Blueprint, request, jsonify, flash, redirect, render_template # all from twitoff, only Flask, json, and request used here
from sklearn.linear_model import LogisticRegression # for example
from sklearn.ensemble import RandomForestClassifier # consider using if no neural net pickle
# import pickle model


# Import Leafly csv                 # import from github URL for production

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly.csv"

df = pd.read_csv(file_name)

strains = df['Strain']


# Mock data for quasi params

MOCK_DATA = {"First Name": "John", "Last Name": "Doe", "Effects": "Euphoric, Happy, Relaxed, Focused"}

#effects = MOCK

# Defining a params dict for parameters to be "sent"(GET) to the front end API. ie: params for First Name, Last Name, and Effects 

PARAMS = {"First Name": first_name, "Last Name": last_name, "effects": effects}


# REQUEST for a JSON object in the following format:

{
    "First Name": ["John"],
    "Last Name": ['Doe'],
    "Effects": ["Euphoric, Happy, Relaxed, Focused"]
}

# RESPONSE is in JSON as a list of dictionaries, each with 3 keys: First Name, Last Name, and Recommendatio

{
    "First Name": "John",
    "Last Name": "Doe",
    "Recommendattion": "Purple Kush"
}


# Flask API

api = Flask(__name__)


# API endpoints

GET_URL = "getaddress"

API_ENDPOINT = "postaddress"

API_KEY = "is this even necessary?"


# GET route

@api.route('/effects', methods=['GET'])
def get_effects_recommend(): # Try using a class here
    if(request.method == 'GET'):

        # Sending GET request and saving the response as (r)esponse object

        r = requests.get(url = GET_URL, params = PARAMS)

        # Extracting data in json format

        data = r.json()

        # Extracting first name, last name, and effects of the first matching

        first_name = data['results'][0]['First Name']
        last_name = data['results'][0]['Last Name']
        effects = data['results'][0]['Effects']

        # Loading the saved pickle model

        #model = load_model()
        #X, y = load_cannabis(return_X_y=True) # mock-up but just to have some data to use when predicting
        #result = model.predict(X[:2 :]) # mock-up from twitoff iris example to be tweaked
        #return str(result)

        # This was training the model on the fly from twitoff
        classifier = LogisticRegression() # for example
        #classifier = RandomForestClassifier() # back up model to try on the fly or train and pickle before
        classifier.fit(effects, strains) # get list of strains from df['Strain"]
        results = classifier.predict(strains)


# POST route

@api.route('/results', methods=['POST'])
def post_results(): # Try using a class here

    # Data to be sent to API

    data = {"api_dev_key":API_KEY, #?
            "First Name":first_name,
            "Last Name":last_name,
            "Reccommendation":results}

    # Sending post request and saving response as response object

    r = requests.post(url = API_ENDPOINT, data = data)

    # Extracting response text

    DB_URL = r.text

    # For fun, to get some output and confirmation

    print("The DB URL is:%s"%DB_URL)


# Run API

if __name__ == '__main__':
    api.run()



# 13 unique effects, being used for predictions of strains

#Euphoric
#Happy
#Relaxed
#Focused
#Energetic
#Sleepy
#Talkative
#Tingly
#Aroused
#Giggly
#Creative
#Hungry
#Uplifted
