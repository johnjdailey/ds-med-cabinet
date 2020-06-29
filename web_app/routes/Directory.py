# Directory.py



# Import

from os import path
import csv
import pandas as pd
from flask import Blueprint, request, render_template
from web_app.Recommend import recommend2


# Make Blueprint for __init__.py

Directory = Blueprint("Directory", __name__)


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "Leafly.csv")

df = pd.read_csv(file_name)

strains = df['Strain']


# App Welcome Page

@Directory.route('/')
def index():
    return render_template("documentation.html", message = "DS Med Cabinet API, using natural language processing to recommend the best cannabis strains to Med Cabinet members.")


# Strain JSON Page

@Directory.route("/data", methods=['GET'])
def data():
    return render_template("json.html")


# Strain Table Page

@Directory.route("/straintable", methods=['GET'])
def straintable():
    return render_template("df.html")


# Route to display dictionary list via template

@Directory.route("/strainmenu", methods=['GET'])
def strainmenu():
    '''
    For loops the Leafly.csv file appending each row to a list.
    Does not include the first line, since that is our headers in the csv file.
    Returning the list via a template.
    '''
    with open(file_name, encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        strains = []
        for row in data:
            if not first_line:
                strains.append({
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                })
            else:
                first_line = False
    return render_template("strainmenu.html", strains=strains)


# When the user visits the reccommendation page

@Directory.route("/recommendations")
def recommendations():
    #print("Recommendations!")

    return render_template("prediction_form.html")


# Makes local recommendations in app for visitors

@Directory.route("/recommendation", methods=["POST"])
def predict():
    print("RECOMMENDATION ROUTE...")
    print("FORM DATA:", dict(request.form))
    
    desired_effects = request.form["desired_effects"]
    #desired_flavors = request.form["desired_flavors"]
    #desired_description = request.form["desired_description"]    

    results = recommend2(desired_effects)

    return render_template("prediction_results.html",
    desired_effects=desired_effects,
    #desired_flavors=desired_flavors,
    #desired_description=desired_description,
    recommendation_strain=results[0],
    recommendation_effects=results[1],
    recommendation_flavor=results[2],
    recommendation_description=results[3],
    recommendation_type=results[4],
    recommendation_rating=results[5]
    )
