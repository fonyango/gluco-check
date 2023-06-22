# Gluco-check
This is a machine learning model REST API that predicts the probability of a user having diabetes based on his/her physiological data.

## Data

The data is from [Kaggle](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset).
The features in the data include:
`Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction`, and `Age`.

## Data processing

The data was processed and explored using various python libraries and frameworks such as `pandas, numpy`, and `scipy`. I also performed various statistical analysis using `statsmodels` library to identify descriptive statistics, correlations and causation before training the machine learning model. Click here to see the notebook used for exploratory data analysis and model training.

Below is a table showing the statistical significance of the independent variables on the dependent variable

![causation-significance](https://github.com/fonyango/gluco-check/assets/39304423/978fe449-5595-4609-a063-d253642c72df)



## Model training

A Logistic Regression model has been trained on the data and achieved the following performance metrics that show that the model has an acceptable predictive power:
- Accuracy: `0.7835`
- Precision: `0.7342`
- Recall: `0.6304`
- F1-score: `0.6784`
- AUC-ROC: `0.829`

## Outcome

The outcome of the prediction is the probability of the user being diagnosed with diabetes. The model outputs this as a percentage. For instance, `78.34%`.

## App testing

To test the API, do the following:

- clone the repository - `git clone https://github.com/fonyango/gluco-check.git`

- install the packages - `pip install requirements.txt`

- run the Django app locally - `python manage.py runserver`

- test the endpoint using [Postman](https://www.postman.com/) as shown in the image below:
  endpoint `predict/`


**Request body**:

![request-body](https://github.com/fonyango/gluco-check/assets/39304423/bc94ebb7-76b2-4272-b037-5e0601f8f662)


**Response body**:

![response-body](https://github.com/fonyango/gluco-check/assets/39304423/a5d94479-61c4-4a16-9253-8b2025add49f)




