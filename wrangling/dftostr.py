# dftostr.py

# df to string format to try to fix unicode errors
# have removed with Regex, but would like to replace with actual characters



# Imports

from os import path
import pandas as pd
import csv
from flask import jsonify


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 10000)

file_name = path.join(path.dirname(__file__), "Leafly.csv")
df = pd.read_csv(file_name)
df = df.to_string()

text_file = open("df.csv", 'w')
text_file.write(str(df.encode()))
text_file.close()
