# dftohtml.py



# Imports

from os import path
import pandas as pd
import csv


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 10000)

file_name = path.join(path.dirname(__file__), "cannabis.csv")
df = pd.read_csv(file_name)
html = df.to_html()

text_file = open("df.html", 'w')
text_file.write(str(html.encode("utf-8")))
text_file.close()
