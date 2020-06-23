# Data Science ML and DE

# Med Cabinet API

This API accepts GET requests like so:

MOCK_DATA = {"id": 420, 
            "First Name": "John", 
            "Last Name": "Doe", 
            "Desired_Effects": "Creative,Uplifted,Tingly,Euphoric,Relaxed, 
            Giggly"}

and then uses the desired effects to predict the best cannabis strain using natural language processing, machine learning. The results are then sent via the API PUT as so:

MOCK DATA = {"id": 420,
             "First Name": 'John',
             "Last_Name": "Doe",
             "Desired_Effects": "Creative,Uplifted,Tingly,Euphoric,Relaxed, Giggly",
             "Recommendation": "Pineapple-Super-Silver-Haze",
             "Recommendation_Effects": "Happy,Euphoric,Energetic,Focused,Tingly"}

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
