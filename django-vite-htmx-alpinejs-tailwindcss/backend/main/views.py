from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html", {})


def htmx_test(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<div>Hello from django server.</div>")

def test_page(request: HttpRequest) -> HttpResponse:
    return render(request, "main/test_page.html", {})