# StrainAPI.py

# http://strains.evanbusse.com/index.html



import os
import requests
import psycopg2
import json, sys
from pprint import pprint
from dotenv import load_dotenv
from psycopg2 import connect, Error


# Load contents of the .env file into the script's environment

load_dotenv()

# Connect to Elephant PG DB

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

# Establish Elephant PG connection

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", conn)

cur = conn.cursor()
print("CURSOR:", cur)


# Load Strain API Key from .env file and make API Get request from Strain API

STRAIN_API_KEY = os.getenv("STRAIN_API_KEY")

url = "http://strainapi.evanbusse.com/%s/strains/search/effect/EFFECT" % STRAIN_API_KEY

response = requests.get(url)
print(type(response)) #> <class 'requests.models.Response'>
print(response.status_code) #> 200
print(type(response.text)) #> <class 'str'>

dict_response = (response.text) # transforms the string response into a usable python datatype (list or dict)
print(type(dict_response)) #> <class 'str'>

# Output the results to the terminal

#pprint(dict_response)

# Use Python to read a JSON file

record_list = json.loads(dict_response)


# Evaluate the object returned by json.loads() to verify that it’s a list 
# and grab the first potential Postgres "record"

if type(record_list) == list:
    first_record = record_list[0]

# Use the Python dictionary’s keys() method to retrieve its “column” names in the form of a list
# Get the column names from the first record

columns = list(first_record.keys())
print ("\ncolumn names:", columns)

# Create the Med_Cabinet Table

cur.execute("CREATE TABLE Med_Cabinet(id INT, name VARCHAR, race VARCHAR, effect VARCHAR)")

# Declare an SQL string for Postgres records

table_name = "Med_Cabinet"
sql_string = 'INSERT INTO {} '.format( table_name )
sql_string += "(" + ', '.join(columns) + ")\nVALUES "

# Use Python to parse a JSON object
# Enumerate over the record

for i, record_dict in enumerate(record_list):

    # Iterate over the values of each record dict object

    values = []
    for col_names, val in record_dict.items():

        # Postgres strings must be enclosed with single quotes

        if type(val) == str:
            
            # Escape apostrophies with two single quotations

            val = val.replace("'", "''")
            val = "'" + val + "'"

        values += [ str(val) ]

    # Join the list of values and enclose record in parenthesis

    sql_string += "(" + ', '.join(values) + "),\n"

# Remove the last comma and end statement with a semicolon

sql_string = sql_string[:-2] + ";"

# Output the results to the terminal

#print ("\nSQL statement:")
#print (sql_string)

# Use psycopg2 to insert JSON data
# Only attempt to execute SQL if cursor is valid

if cur != None:

    try:
        cur.execute( sql_string )
        conn.commit()

        print ('\nfinished INSERT INTO execution')

    except (Exception, Error) as error:
        print("\nexecute_sql() error:", error)
        conn.rollback()

    # Close the cursor and connection

    cur.close()
    conn.close()

    # If you want to remove all the inserted records from the Postgres table you can execute a 
    # TRUNCATE TABLE table_name statement in ElephantSQL, followed by the table name, and all of the records will be deleted.
