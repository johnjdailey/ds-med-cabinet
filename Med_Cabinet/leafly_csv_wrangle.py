# leafly_csv_wrangle.py

# First wrangle to get unique effects for front end user survey and ML use



import pandas as pd


# Import Leafly csv

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\cannabis.csv"

df = pd.read_csv(file_name)

# Examine the Leafly csv data head

#print(df.head())


# Check type of Effects column data

print(type(df.Effects[1])) # <class 'str'>


# Strip and split the Effects column string data in order to get unique values

df.Effects.str.strip('[]').str.split(',')

stripped_effects = list(set([a for b in df.Effects.str.strip('[]').str.split(',') for a in b]))

# Verify the Effects column data had changed from string to set to list

print(type(stripped_effects))


# Function to get unique values 

def unique(effects): 
      
    # Insert the list to the set 

    effects_set = set(stripped_effects) 

    # Convert the set to the list 

    unique_list_of_effects = (list(effects_set)) 
    for x in unique_list_of_effects: 
        print(x)

print(unique(stripped_effects)) 

# 13 Unique Effects

#Dry Mouth
#Euphoric
#Happy
#Relaxed
#Focused
#Energetic
#Sleepy
#Talkative
#Tingly
#Aroused
#Giggly
#Creative
#Hungry
#Uplifted
