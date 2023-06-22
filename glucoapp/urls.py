from django.urls import path, include
from .views import predictViewset

urlpatterns = [
    path('predict/', predictViewset.as_view({'post':'get_prediction_probability'}), name='probabilities'),
]