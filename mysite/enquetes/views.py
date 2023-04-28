from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! Você está no índice da enquete")
# Create your views here.
