from django.shortcuts import render

# Create your view
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. You're at  the quiz index")

