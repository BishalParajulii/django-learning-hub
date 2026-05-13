from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from app.models import Jokes
from app.serializers import JokeSeriazers
from apis.phone import fetch_phone_number
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def jokes(request):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    return JsonResponse(data)

def joke_page(request):
    return render(request, 'app/index.html')


class JokesViewSet(viewsets.ModelViewSet):
    queryset = Jokes.objects.all()
    serializer_class = JokeSeriazers
    


@api_view(['POST'])
def validate_phone(request):
    phone = request.data.get('phone')

    if not phone:
        return Response({"error": "Phone number is required"}, status=400)

    if len(phone) == 10 and phone[0] == "9":
        phone = "+977" + phone

    result = fetch_phone_number(phone)

      

    
    if not result or "error" in result:
        return Response({
            "error": result.get("error") if result else "No response from API",
            "raw": result
        }, status=400)

    return Response({
        "phone": result.get("phone_number"),
        "valid": result.get("phone_validation", {}).get("is_valid"),
        "carrier": result.get("phone_carrier", {}).get("name"),
        "line_type": result.get("phone_carrier", {}).get("line_type"),
        "country": result.get("phone_location", {}).get("country_name"),
        "breaches": result.get("phone_breaches", {}).get("total_breaches"),
    })