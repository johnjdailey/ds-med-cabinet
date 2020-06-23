# Recommend function



import pandas as pd
import pickle
import json



# Import Leafly csv

#df = pd.read_csv('data/Leafly.csv')

file_name = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\data\Leafly.csv"

df = pd.read_csv(file_name)


# Import pickled model

model_path = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\pickles\nn.P"

NN_model = pickle.load(open(model_path, 'rb'))
#NN_model = pickle.load(open('nn.P', 'rb'))
#NN_model = load_model()


# Import pickled vectorizer

vectorizer_path = r"C:\Users\johnj\OneDrive\Documents\Lambda\BuildWeek3\data-science\Med_Cabinet\pickles\tfidf.P"

tfidf = pickle.load(open(vectorizer_path, 'rb'))


# Recommend function

def recommend(user_input):
    temp_df = NN_model.kneighbors(tfidf.transform([user_input]).todense())[1]
    

    #print(temp_df)
    
    for i in range(4):
        info = df.loc[temp_df[0][i]]['Strain']
        #info = info.to_json()
        #info_name = {f'strain_{i+1}':info}
        #strains_info.update(info_name)
        print(json.dumps(info))

        #return json.dumps(info) #for engineers, the return does not work in jupyter lab.  Should work in vsCode.
