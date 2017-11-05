from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting_view(request):
    return HttpResponse("Hello World")

def goodbye_view(request):
    return HttpResponse("Goodbye Cruel World")
