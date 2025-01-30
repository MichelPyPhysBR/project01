from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Home")

def contact(request):
    return HttpResponse("Contato")

def about(request):
    return HttpResponse("sobre")