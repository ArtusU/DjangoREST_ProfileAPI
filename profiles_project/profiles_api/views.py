from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View.""" 

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview =[
            'Defines functions that maches standard Http methods',
            'Uses HTTP methods as function (get, path, put, delete)',
            'It is similar to the traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
         ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
