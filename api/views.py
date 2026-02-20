from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.automation import main


@api_view(['GET'])
def simple_response(request):
    return Response({"message": "OK"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def convert(request):
    mode = request.POST.get("mode", "api")

    if mode == "api":
        data = getDataAPI(request)
        if data["error"] != "":
            return Response(data["error"], status=status.HTTP_400_BAD_REQUEST)
        try:
            response = main.generateAlleasyFromAPI(data)
        except ValueError as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response(f"Erro ao buscar dados da API 7pace: {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        data = getDataExcel(request)
        if data["error"] != "":
            return Response(data["error"], status=status.HTTP_400_BAD_REQUEST)
        response = main.generateAlleasyExcel(data)

    return Response(response, status=status.HTTP_200_OK)


def home(request):
    return render(request, 'home.html')


def getDataAPI(request):
    name = request.POST.get("name", "")
    date = request.POST.get("date", "")
    if name == "":
        return {"error": "name"}
    if date == "":
        return {"error": "date"}
    return {"name": name, "date": date, "error": ""}


def getDataExcel(request):
    base64 = request.POST.get("base64", "")
    name = request.POST.get("name", "")
    date = request.POST.get("date", "")
    if name == "":
        return {"error": "name"}
    if date == "":
        return {"error": "date"}
    if base64 == "":
        return {"error": "base64"}
    return {"base64": base64, "name": name, "date": date, "error": ""}
