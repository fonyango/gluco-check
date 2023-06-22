# Gluco-check
This is a machine learning model REST API that predicts the probability of a user having diabetes based on his/her physiological data.

## Faatures
The features in the data include:
`Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction`, and `Age`.

## Outcome

The outcome of the prediction is the probability of the user being diagnosed of diabetes. The model outputs this as a percentage.

## Model training

The model has been trained on 768 data point and has achieved the following performance metrics that shows the model has an acceptable predictive power:
- Accuracy: `0.7835`
- Precision: `0.7342`
- Recall: `0.6304`
- F1-score: `0.6784`
- AUC-ROC: `0.829`

## App testing

To test the API, do the following:

clone the reposiroty - `git clone https://github.com/fonyango/gluco-check.git`

install the packages - `pip install requirements.txt`

run the django app locally - `python manage.py runserver`

test the endpoint using postman as shown in the image below:


