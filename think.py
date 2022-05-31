# Import dependancies
import joblib
from sklearn.preprocessing import StandardScaler
import requests
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd

# Create an API request using the link provided by asterank to gather data
url = "http://asterank.com/api/asterank?query=" 
response = requests.get(url + '{"price":{"$lt":1, "$gt":0}}&limit=1000').json()
# Data retrieval is limited to 1000 rows by default and can not be changed (by design)

# Create dataframe using data retrieved by the request above
df = pd.DataFrame(response)
df = df.sort_values(by = 'price' , ascending = False)

# Second request to get more data into the final dataframe
response2 = requests.get(url + '{"price":{"$gt":1}}&limit=1000').json()
df2 = pd.DataFrame(response2)

# Using only colummns we felt were necessary for our project
neo_df = df[['full_name', 'spec' , 'class' , 'ad' , 'q' , 'a' , 'e' , 'dv' ,'per' , 'price' , 'profit' , 'moid' , 'diameter']]
neo_df2 = df2[['full_name', 'spec' , 'class' , 'ad' , 'q' , 'a' , 'e' , 'dv' ,'per' , 'price' , 'profit' , 'moid' , 'diameter']]


# Merging both datasets by appending
merged_df = neo_df.append(neo_df2)


# Replacing empty cells with 'nan' to be able to drop eaier later
new_df = merged_df.replace('', np.nan, inplace=False)


# Dropping all null values
new_df = new_df.dropna()


# Creating a row with 0 and 1 as values to be able to run machine learning models using this data
new_df['profitable'] = (new_df['profit'] > 1).astype(int)
new_df['diameter'] = new_df['diameter'].astype(float)
new_df.to_csv('asteroid_data.csv', header = True)

# Define our variables to use in our model
X = new_df.drop(['full_name','profit','price','spec', 'class','profitable'], axis =1)
y = new_df['profitable']

# Converting categorical data into a numeric format
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Scaling the data for best results
scaler = StandardScaler().fit(X_train)

# Define the function for the flask app to use our ml algorithm
def thinker(num):
    
    # Created a container for our output
    output = []

    # Defined the url to the website where we make api calls to
    url = "http://asterank.com/api/asterank?query="

    # Define the response 
    response = requests.get(url + '{"dv":{"$gt":0}}&limit=' + num).json()

    # Scaling the data live as it is being read in on a loop
    asteroid_test = scaler.transform(np.array([response[0]['ad'],
                            response[0]['q'], 
                            response[0]['a'], 
                            response[0]['e'], 
                            response[0]['dv'], 
                            response[0]['per'], 
                            response[0]['moid'], 
                            response[0]['diameter']]).reshape(1,-1))
    
    # Reshaoping and scaling data to be fed into our output for loop
    for n in range(1,int(num)):
        asteroid_test2 = np.array([response[n]['ad'],
                        response[n]['q'], 
                        response[n]['a'], 
                        response[n]['e'], 
                        response[n]['dv'], 
                        response[n]['per'], 
                        response[n]['moid'], 
                        response[n]['diameter']]).reshape(1,-1)
        asteroid_test = np.append(asteroid_test, scaler.transform(asteroid_test2),0)

    # Loading the model we chose to use for this data
    rf_model = joblib.load("ml_models/rf_model.joblib")
    test = rf_model.predict(asteroid_test)
    num_accurate = 0

    # Iterate through above ml outputs and convert binary outputs into non-numerical words
    for n in range(int(num)):
        output.append(f"Actual: $ {response[n]['profit']}<br>")
        if test[n] == 0:
            output.append(f"Prediction: No Profit <br>")
        else:
            output.append(f"Prediction: Profit <br>")    
        if (test[n] == 0 and response[n]['profit']<1) or (test[n] == 1 and response[n]['profit']>1):
            output.append('Accurate<br>')
            num_accurate +=1
        else:
            output.append('Inaccurate<br>')
        output.append("--------------------<br>")
    output.append(str((num_accurate/int(num))*100)+'% accurate')

    # Converting our data into the string format to be able to use for our return in our flask app
    final = ""

    for line in output:
        final = final+line

    return final
