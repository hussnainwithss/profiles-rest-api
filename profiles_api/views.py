from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication


from .seralizers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile
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
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(ViewSet):
    """Example view set"""
    seralizer_class = HelloSerializer

    def list(self, request):
        a_viewset = [
            'Uses HTTP methods as function (list, create, retrieve, updat, partial_update)',
            'Auto maps URLS to routers',
            'more power less code'
        ]
        return Response({'message': 'Django REST API', 'a_viewset': a_viewset})

    def create(self, request):
        """"Create a new hello message"""
        serializer = self.seralizer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting object by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating object by id"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle partialy updating object by id"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle partialy updating object by id"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(ModelViewSet):
    """Handles creating updating user profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
