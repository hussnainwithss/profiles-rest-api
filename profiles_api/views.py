from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .seralizers import HelloSerializer
# Create your views here.


class HelloApiView(APIView):
    """ helloworld api view for testing"""
    seralizer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns response of the get response to API"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'Gives you most control over your app logic'
        ]
        return Response({'message': 'Django REST API', 'an_apiview': an_apiview})

    def post(self, request):
        """Handles post requests made to the api"""
        # print(request.data)
        serializer = self.seralizer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Handle deletion of an object"""
        return Response({'method':'DELETE'})