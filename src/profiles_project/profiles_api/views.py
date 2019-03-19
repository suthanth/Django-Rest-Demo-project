from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.
class HelloApiView(APIView):
    """Test Api View."""

    serialzer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns api view format"""

        an_apiview = [
            'Http method',
            'Test APi view'
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Creates serialized object"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Updates an object"""

        return Response({"method":"put"})

    def patch(self, request, pk=None):
        """Updates the specified fields"""

        return Response({"method":"patch"})

    def delete(self, request,pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Creating Hello view set"""

    def list(self, request):
        """Returns a hello message"""

        a_viewset = [
            'uses actions(list, create, retrieve, update, partial update)',
            'Automatically maps to URLS using routers',
            'provides more functionality with less code'
        ]

        return Response({'message':'hello', 'a_viewset':a_viewset})
