from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse ("<h1>ruturaj is captain of csk</h1>")

def wicketkeeper(request):
    return HttpResponse("<h1>dhoni is wicket keeper of csk</h1>")

def vicecaptain(request):
    return HttpResponse("<h1>jadeja is vice captain of csk</h1>")
