# test_Flask_API.py

# This is the test version of the API, it can both GET JSON and POST data 

# The NLP model is imported as the recommend function. Run the model, and test sending results



#Imports

import pandas as pd
import requests
from flask import Flask, Blueprint, json, request, jsonify
#from flask_restful import Api
from Recommend import recommend


# Flask API

app = Flask(__name__)
#api = Api(app)


# A welcome message to app

@app.route('/')
def index():
    return "Welcome to the DS-Med-Cabinet API"


@app.route('/predict', methods=['GET', 'PUT'])
def get_predict_post():

    # GET JSON User Data

    if request.method=='GET':
        
        # Request .json from Web

        get_data = request.json
        
        # Extracting id, first name, last name, and effects from the json get_data
    
        user_id = get_data["id"] 
        first_name = get_data["First Name"]
        last_name = get_data["Last Name"]
        effects = get_data["Effects"]
        
        # Make recommendation

        results = recommend(effects)
        
        # Return results

        return results
        
        # Insomnia Test
        #return get_data # This works, got the JSON from insomnia
        

    # POST JSON User Data and Recommendation

    elif request.method=='PUT':

       # User Data to be sent to backend API

        post_data = {"id": user_id,
                    "First Name": first_name, 
                    "Last Name": last_name,
                    "Desired_Effects": effects, 
                    "Reccommendation": results}

        # Recommendation

        reccommendation = json.dumps(post_data) #(post_data, indent=2, separators=(', ', ': '))
        
        return reccommendation

        # Insomnia Test
        #return {"id": 420"
        #        "First Name": 'John',   # This works
        #        "Last_Name": "Doe",
        #        "Recommendation": 'results'}


    else:
        return("Ok, waiting.")


# Run API

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
