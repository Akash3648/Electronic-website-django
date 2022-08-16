from django.http import HttpResponse 
from django.shortcuts import render

def homePage(request):
    return HttpResponse("Welcome to Home")

def renderPage(request):
    return render(request, "first.html")