from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.automation import main


@api_view(['GET'])
def simple_response(request):
    return Response({"message": "OK"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def convert(request):
    data = getData(request)
    if data["error"] != "":
        return Response(data["error"], status=status.HTTP_400_BAD_REQUEST)

    response = main.generateAlleasyExcel(data)
    return Response(response, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'home.html')


def getData(request):
    base64 = request.POST.get("base64", "")
    name = request.POST.get("name", "")
    date = request.POST.get("date", "")
    if name == "":
        response = {"error": "name"}
        return response
    if date == "":
        response = {"error": "date"}
        return response
    if base64 == "":
        response = {"error": "base64"}
        return response
    response = {
        "base64": base64,
        "name": name,
        "date": date,
        "error": ""
    }
    return response
