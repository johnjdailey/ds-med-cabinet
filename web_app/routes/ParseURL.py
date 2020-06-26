# ParseURL.py

'''
Code here was built with inspiration from this article:
https://medium.com/@kellylougheed/make-a-flask-app-with-a-csv-as-a-flat-file-database-373632a2fba4
 
'''


from os import path
import csv
from flask import Flask, Blueprint, render_template, jsonify


# Make Blueprint for __init__.py

ParseURL = Blueprint("ParseURL", __name__)


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "Leafly.csv")


# Route to display dictionary list

@ParseURL.route("/request", methods=['GET'])
def row():
    '''
    For loops the cannabis.csv file appending each row to a list.
    Does not include the first line, since that is our headers in the csv file.
    Returning that list.
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
    return jsonify(strains)


# Route to display single dictionary list item as JSON object

@ParseURL.route('/<strain>', methods=['GET'])
def strain_url(strain):
    '''
    Parameters: name of strain from database as a string.
    For loops the cannabis.csv file, creating a dictionary.
    Returning only the strain that was given as a parameter.
    '''
    with open(file_name, encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        dict_strain = {}
        for row in data:
            if row[0] == strain:
                dict_strain = {
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                }
                break
    return jsonify(dict_strain)


# Route to display single dictionary list item via template

@ParseURL.route("/<strain>/strainmenu", methods=['GET'])
def pretty_url(strain):
    '''
    Parameters: name of strain from database as a string.
    For loops the cannabis.csv file appending each row to a list.
    Returning only the strain that was given as a parameter.
    '''
    with open(file_name, encoding="utf8") as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        strains = []
        for row in data:
            if row[0] == strain:
                strains.append({
                    "strain": row[0],
                    "type": row[1],
                    "rating": row[2],
                    "effects": row[3],
                    "flavor": row[4],
                    "description": row[5]
                })
                break
    return render_template("strainmenu.html", strains=strains)
