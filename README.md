# data-science

# Med Cabinet


# StrainAPItoPG.py

Pulls approximately 24,393 rows of medical cannabis data from Strain API including:

id, name, race, effect ... as column headers.

The remainder of the code includes creating a connection to a Postgres Database hosted on ElephantSQL and storing the pulled Strain API data there, for analysis by DS in conjuncture with front end "form data" from the user that is submitted to the DS API for analysis, aka modeling and strain recommendation.


# StrainAPI.csv

CSV file from StrainAPI data in Postgres DB.


# Leafly.csv

Leafly data from Kaggle


# Leafly_nolistcommas.csv

Leafly data wrangled with no list and commas in effects column


# Leafly_csv_wrangle.py

First wrangle on the Leafly "Leafly.csv" data to discover 13 useful unique "effects" values for Front End user survey for relaying user input via app/API to the final pickled ML model for predictions, which are to be POSTed and stored in the BE PG DB.

Second wrangle is to strip "[]"" from list of Effects in Effects column values and replace "," with " " while also turning the list into a pandas.core.series in attempt for better neural networking fit. Output as Leafly_nolistcommas.csv

# processing_data.ipynb

Processing Leafly data (cannabis.csv) to perform baseline model. "#to be pickled.... #nn, dtm, tfidf"

