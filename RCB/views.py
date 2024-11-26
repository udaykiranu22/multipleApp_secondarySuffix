from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse ("<h1>kohli is captain of rcb</h1>")

def wicketkeeper(request):
    return HttpResponse("<h1>salt is wicket keeper of rcb</h1>")

def vicecaptain(request):
    return HttpResponse("<h1>patidhar is vice captain of rcb</h1>")