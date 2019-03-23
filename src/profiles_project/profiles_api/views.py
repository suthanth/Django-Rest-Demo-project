from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers
from . import models
from . import permissions
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

    def create(self, request):
        """creates a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "hello {0}".format(name)
            return Response({"message":message})

        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """retrieve the message"""

        return Response({'Http method':'GET'})

    def update(self, request, pk=None):
        """Handles updating of an object"""

        return Response({"http method":"PUT"})

    def partial_update(self, request, pk=None):
        """Handles partial update """

        return Response({"http method":"patch"})

    def destroy(self, request, pk=None):
        """destroy an objects"""

        return Response({"http method":"delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Create, read and update UserProfile """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
