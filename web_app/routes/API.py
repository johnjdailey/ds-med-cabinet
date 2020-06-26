# POST_PUT_API.py

# This is the test version of the API, it can both POST and PUT JSON data 

# An NLP model is imported as the recommend function, recommends strains and sends results



#Imports

import pandas as pd
import requests
import json
from flask import Blueprint, request, jsonify, render_template
from web_app.Recommend import recommend


# Make Blueprint for __init__.py

API = Blueprint("API", __name__)


# POST_PUT_API template

@API.route('/predict', methods=['POST', 'PUT'])
#def template():
#    return render_template("predict.html", message = "DS Med Cabinet API using natural language processing to recommend the best cannabis strains to Med Cabinet members.")


# POST_PUT_API post_predict_put

def post_predict_put():

    # POST JSON User Data

    if request.method=='POST':
        
        # Request .json from Web

        post_data = request.json
        
        # Extracting id, first name, last name, and effects from the json post_data
    
        user_id = post_data["id"] 
        #first_name = post_data["First Name"]
        #last_name = post_data["Last Name"]
        effects = post_data["Effects"]
        
        # Make recommendation

        results = recommend(effects)
        
        # Return results

        return results
        

    # PUT JSON User Data and Recommendation

    elif request.method=='PUT':

       # User Data to be sent to backend API

        put_data = {"id": 420, #user_id,
                    #"First Name": first_name, 
                    #"Last Name": last_name,
                    "Desired_Effects": "Happy,Relaxed,Uplifted,Focused,Aroused", #effects, 
                    "Reccommendation": "Captain-America-Og"} #results}

        # Recommendation

        reccommendation = put_data #(put_data, indent=2, separators=(', ', ': '))
        
        return jsonify(reccommendation)


    else:

        return ("OK, waiting")
