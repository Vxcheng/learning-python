from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1 style='color:blue;'>Hello, Django! 🎉</h1>")
