# Directory.py



# Import

from os import path
import pandas as pd
from flask import Blueprint, render_template
from werkzeug.routing import BaseConverter


# Make Blueprint for __init__.py

Directory = Blueprint("Directory", __name__)


# Import Leafly csv

file_name = path.join(path.dirname(__file__), "Leafly.csv")

df = pd.read_csv(file_name)

strains = df['Strain']


# App Welcome Page

@Directory.route('/')
def index():
    return render_template("home.html", message = "DS Med Cabinet API, using natural language processing to recommend the best cannabis strains to Med Cabinet members.")


# Strain JSON Page

@Directory.route("/strainjson")
def strainjson():
    return render_template("json.html")


# Strain Table Page

@Directory.route("/straintable")
def straintable():
    return render_template("df.html")


# Custom converter

class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)
                        for value in values)


# Flask Url-converter

@Directory.route('/<strain>')
def strain_url(strain):
    """Show all of the posts for the given strain."""
    strain = []
    for strain in strains:
        strain = strain in strains

    return render_template('json.html', strain=strain)
