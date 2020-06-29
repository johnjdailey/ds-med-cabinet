# DS Med Cabinet API

An API that receives user inputs as a json object, uses a natural language processing model to recommend the best cannabis strain based on desired user effects, and returns a recommendation as a json object.

# API URL

https://ds-med-cabinet.herokuapp.com/predict

This API accepts POST and PUT requests like so:

```
MOCK DATA = {"id": 420,
            "Desired Effects": "Creative,Uplifted,Tingly,Euphoric,Relaxed, 
            Giggly"}
```

and then uses the desired effects to predict the best cannabis strain using natural language processing, machine learning. The results are then sent to the DB via the API PUT as so:

```
MOCK DATA = {"id": 420,
             "Recommendation": "Pineapple-Super-Silver-Haze"}
```

The API can also PUT more data pertaining to the recommendation including type, rating, flavor, description, and this is the MVP.


# Data

# Leafly.csv

Leafly data from Kaggle


# Pickles

# nn.pkl

Nearest Neighbor trained model and pickled to make predictions in a virtual environment.

# tfidf.pkl

Vectorizer model to vectorize the words in the data so the the Nearest Neighbor model can make better predictions.


# web_app

# __init__.py

Initializes the Flask App

# Recommend.py

Where the data, pickles, and recommend function come together to make NLP predictions for the API.

# Flask API

GET user input data for making predictions, and PUT results and recommendations to the database.
