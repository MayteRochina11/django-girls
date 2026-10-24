from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse


def obtener_info_pythonanywhere(request):
    api_key = settings.PYTHONANYWHERE_API_KEY
    username = settings.PYTHONANYWHERE_USERNAME

    url = (
        f"https://www.pythonanywhere.com/api/v0/user/{username}/cpu/"
    )
    headers = {"Authorization": f"Token {api_key}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json())
    return JsonResponse(
        {"error": "No se pudo obtener la información"}, status=response.status_code
    )