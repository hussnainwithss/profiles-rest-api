from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """ helloworld api view for testing"""

    def get(self, request, format=None):
        """Returns response of the get response to API"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'Gives you most control over your app logic'
        ]
        return Response({'message': 'Django REST API', 'an_apiview': an_apiview})
