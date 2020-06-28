# Leafly_csv_Wrangle.py

# First wrangle to get unique effects for front end user survey and ML use
 
# Second wrangle to strip "[]"" from list of Effects in Effects column values
# and replace "," with " " in attempt for better neural networking fit.



# Imports

import pandas as pd


# Import Leafly csv

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly.csv"

df = pd.read_csv(file_name)

# Examine the Leafly csv data head

#print(df.head())


# First wrangle for unique effects

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

# Commented out as job is done, and on to second wrangle

#print(unique(stripped_effects))

# 13 Unique Effects

# Dry Mouth - Not desireable, not included in 13
# Euphoric
# Happy
# Relaxed
# Focused
# Energetic
# Sleepy
# Talkative
# Tingly
# Aroused
# Giggly
# Creative
# Hungry
# Uplifted


# Second wrangle

# Make the stripped, split and replace in Effects column persist (uses strip and split from Wrangle 1)

df["Effects"] = df["Effects"].str.replace(","," ").astype(str)

# Check type after strip and split, which is <class 'pandas.core.series.Series'>

print(type(df['Effects']))

# Verify changes with printout to terminal

print(df['Effects'].head())

# Set pandas option to show all columns in final printout verification

pd.set_option('display.max_columns', None)

print(df.head())

# Export csv for testing in neural network baseline

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly_nolistcommas.csv"

df.to_csv(file_name, sep='\t', encoding='utf-8')
