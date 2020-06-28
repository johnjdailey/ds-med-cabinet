# dftojson.py


# Imports

from os import path
import csv
import json


file_path = r'C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\cannabis.csv'

csvfile = open(file_path, encoding="utf8")
jsonfile = open('cannabis.json', 'w')


fieldnames = ("Strain", "Type", "Rating", "Effects", "Flavor"," Description")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
