# Directory.py



# Import

from os import path
import csv
import pandas as pd
from flask import Blueprint, render_template


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

@Directory.route("/strainjson", methods=['GET'])
def strainjson():
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
