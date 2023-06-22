import joblib
import pandas as pd
import numpy as np

model = joblib.load('model.pkl')


def predict_diabetes(user_details):
    """
    get probability fo someone having diabetes
    """
    data = pd.Series(user_details)
    input_data = pd.DataFrame(data).transpose()

    # Add a constant feature
    input_data.insert(0, 'const', np.zeros(len(input_data)))
    prediction = model.predict_proba(input_data)[:,1]
    
    prediction = prediction[0]
    
    result = round(prediction * 100,2)

    return result
