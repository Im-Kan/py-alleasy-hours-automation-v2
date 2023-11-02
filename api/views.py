from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def simple_response(request):
    return Response({"message": "OK"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def convert(request):
    return Response(":)", status=status.HTTP_200_OK)

def home(request):
    return render(request, 'home.html')