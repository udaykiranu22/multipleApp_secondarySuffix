from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse ("<h1>cummins is captain of srh</h1>")

def wicketkeeper(request):
    return HttpResponse("<h1>klassen is wicket keeper of srh</h1>")

def vicecaptain(request):
    return HttpResponse("<h1>nithish is vice captain of srh</h1>")
