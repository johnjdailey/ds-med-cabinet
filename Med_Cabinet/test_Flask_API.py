# test_Flask_API.py

# This is the test version of the API, it can both GET JSON and POST data 

# Next, the NLP model pickle needs to be imported, run the model, and test sending results



#Imports

import pandas as pd
import requests
from flask import Flask, json, request, jsonify
from flask_restful import Api
import pickle

from sklearn.linear_model import LogisticRegression # for example, but need to embed data
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

model = pickle.load(open('nnpickle_file', 'rb'))


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
        
        #return results
        return get_data # This works, got the JSON from insomnia
        

    elif request.method=='POST':

       # Data to be sent to backend API

       #post_data = {"First Name": first_name, 
       #            "Last Name": last_name, 
       #            "Reccommendation": results}

        #reccommendation = json.dumps(post_data) #(post_data, indent=2, separators=(', ', ': '))
        
        #return reccommendation

        #post_data = "Hello World" # This works, printed "Hello World" in Insomnia
        #return post_data
        
        return {"First Name": 'John',   # This also works, good to go, get the model, predict, test.
                "Last_Name": "Doe",
                "Reccommendation": 'results'}


    else:
        return("Ok, waiting.")


# Run API

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
