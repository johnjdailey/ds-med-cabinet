# GET_PUT_API.py

# This is the test version of the API, it can both GET and POST JSON data 

# An NLP model is imported as the recommend function, recommends strains and sends results



#Imports

import pandas as pd
import requests
import json
from flask import Blueprint, request, jsonify, render_template
from web_app.Recommend import recommend


# Make Blueprint for __init__.py

GET_PUT_API = Blueprint("POST_PUT_API", __name__)


# GET_PUT_API template

@GET_PUT_API.route('/predict', methods=['POST', 'PUT'])
#def template():
#    return render_template("predict.html", message = "DS Med Cabinet API using natural language processing to recommend the best cannabis strains to Med Cabinet members.")


# GET_PUT_API get_predict_put

def get_predict_put():

    # GET JSON User Data

    if request.method=='POST':
        
        # Request .json from Web

        get_data = request.json
        
        # Extracting id, first name, last name, and effects from the json get_data
    
        user_id = get_data["id"] 
        #first_name = get_data["First Name"]
        #last_name = get_data["Last Name"]
        effects = get_data["Effects"]
        
        # Make recommendation

        results = recommend(effects)
        
        # Return results

        return results
        

    # PUT JSON User Data and Recommendation

    elif request.method=='PUT':

       # User Data to be sent to backend API

        post_data = {"id": user_id,
                    #"First Name": first_name, 
                    #"Last Name": last_name,
                    "Desired_Effects": effects, 
                    "Reccommendation": results}

        # Recommendation

        reccommendation = json.dumps(post_data) #(post_data, indent=2, separators=(', ', ': '))
        
        return reccommendation


    else:
        return ("OK, waiting.")
