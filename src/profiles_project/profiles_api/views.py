from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test Api View."""

    def get(self, request, format=None):
        """Returns api view format"""

        an_apiview = [
            'Http method',
            'Test APi view'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
