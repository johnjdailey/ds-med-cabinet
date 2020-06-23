# GET_PUT_API.py

# This is the test version of the API, it can both GET and POST JSON data 

# An NLP model is imported as the recommend function. Recommend strains and sends results



#Imports

import pandas as pd
import requests
import json
from flask import Blueprint, request, jsonify
from web_app.Recommend import recommend


GET_PUT_API = Blueprint("GET_PUT_API", __name__)


# Flask API

#app = Flask(__name__)
#api = Api(app)


# A welcome message to app

@GET_PUT_API.route('/')
def index():
    return ("Welcome to the DS-Med-Cabinet API")


@GET_PUT_API.route('/predict', methods=['GET', 'PUT'])
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
        

    # PUT JSON User Data and Recommendation

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


    else:
        return ("Ok, waiting.")


# Run API

#if __name__ == '__main__':
    #app.run(debug=True)
    #app.run()