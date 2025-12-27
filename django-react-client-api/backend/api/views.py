from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "api/index.html")

def message(request, message: str) -> JsonResponse:
    return JsonResponse({"message": f"Your message was {message}"})