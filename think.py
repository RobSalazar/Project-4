# Import dependancies
import joblib
from sklearn.preprocessing import StandardScaler

# Define the function for the flask app to use
def think():

    scaler = StandardScaler()

    response = 

    asteroid_test = scaler.transform(np.array([response[0]['ad'],
                            response[0]['q'], 
                            response[0]['a'], 
                            response[0]['e'], 
                            response[0]['dv'], 
                            response[0]['per'], 
                            response[0]['moid'], 
                            response[0]['diameter']]).reshape(1,-1))

    rf_model = joblib.load("ml_models/rf_model.joblib")
    test = rf_model.predict(asteroid_test)
    num_accurate = 0
    for n in range(num):
        print(response[n]['profit'])
        print(test[n])
        if (test[n] == 0 and response[n]['profit']<1) or (test[n] == 1 and response[n]['profit']>1):
            print('accurate')
            num_accurate +=1
        else:
            print('inaccurate')
        print("--------------------")
    print(str((num_accurate/num)*100)+'% accurate')