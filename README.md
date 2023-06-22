# Gluco-check
This is a machine learning model REST API that predicts the probability of a user having diabetes based on his/her physiological data.

## Data

The data is from [Kaggle](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset).
The features in the data include:
`Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction`, and `Age`.

## Outcome

The outcome of the prediction is the probability of the user being diagnosed with diabetes. The model outputs this as a percentage.

## Model training

The model has been trained on 768 data points and has achieved the following performance metrics that show the model has an acceptable predictive power:
- Accuracy: `0.7835`
- Precision: `0.7342`
- Recall: `0.6304`
- F1-score: `0.6784`
- AUC-ROC: `0.829`

## App testing

To test the API, do the following:

- clone the repository - `git clone https://github.com/fonyango/gluco-check.git`

- install the packages - `pip install requirements.txt`

- run the Django app locally - `python manage.py runserver`

- test the endpoint using [Postman](https://www.postman.com/) as shown in the image below:
  endpoint `predict/`
  Request Body:

![Screenshot from 2023-06-22 11-57-52](https://github.com/fonyango/gluco-check/assets/39304423/2d488752-5695-40bc-900c-bae1b3668f77)

Response body:

![Screenshot from 2023-06-22 11-58-29](https://github.com/fonyango/gluco-check/assets/39304423/1639cd7c-6dea-45cf-8103-bd1b65d64dc1)



