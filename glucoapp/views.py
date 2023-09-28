from rest_framework.response import Response
from rest_framework import viewsets, status
from .predictions import predict_diabetes

class predictViewset(viewsets.ViewSet):
    def get_prediction_probability(self, request):
        """
        returns the probability of someone having diabetes
        """
        try:
            if request.method=='POST':
                user_details = request.data['user_details']

                prediction = predict_diabetes(user_details)

                return Response({
                                    "Success": True, 
                                    "Status": status.HTTP_200_OK, 
                                    "Message": "Successful", 
                                    "Payload": f"Based on your details, you have {prediction}% chance of having diabetes. Please note that this is a prediction and doesn't neccesarilly mean you have diabetes. It is advisable to visit a medical facility for a thorough medical test. Your health matters!"
                                })
            else:
                return Response({
                                    "Success": False, 
                                    "Status": status.HTTP_405_METHOD_NOT_ALLOWED, 
                                    "Message":"Method Not Allowed",
                                    "Payload":None
                                })

        except Exception as e:
            print(e)
            return Response({
                                "Success": False, 
                                "Status": status.HTTP_501_NOT_IMPLEMENTED, 
                                "Message":"An error was encountered during execution"
                            })