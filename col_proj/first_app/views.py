from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func1(request):
    return HttpResponse("Это первая функция")

def func2(request):
    return HttpResponse("Это вторая функция")