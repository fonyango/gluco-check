from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import predictViewset
from .predictions import predict_diabetes


class TestPredictionModule(TestCase):

    def setUp(self):
        self.user_details ={"Pregnancies":6,"Glucose":120,
                            "BloodPressure":100,"SkinThickness":52,
                            "Insulin":72, "BMI":29,"DiabetesPedigreeFunction":1.2,"Age":32}

    def test_prediction(self):
        prediction  = predict_diabetes(self.user_details)
        self.assertIsInstance(prediction, float)

class TestPredictViewSet(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_get_prediction_probability(self):
        view = predictViewset.as_view({"post":"get_prediction_probability"})
        user_details = {"user_details":{"Pregnancies":6,"Glucose":120,"BloodPressure":100,"SkinThickness":52,
             "Insulin":72, "BMI":29,"DiabetesPedigreeFunction":1.2,"Age":32}}
        request = self.factory.post('predict/',user_details, format='json')
        response = view(request)
        self.assertEqual(response.data['Status'], status.HTTP_200_OK)
        self.assertEqual(response.data['Success'], True)
        self.assertEqual(response.data['Message'], "Successful")

    def test_get_prediction_probability_get(self):
        view = predictViewset.as_view({"get":"get_prediction_probability"})
        request = self.factory.get('predict/')
        response = view(request)
        self.assertEqual(response.data['Status'], status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data['Success'], False)
        self.assertEqual(response.data['Message'], "Method Not Allowed")


