from django.shortcuts import render
from django.template import RequestContext


def home(request):
    cd = {}
    return render(request, 'www/home.html')

def copyright(request):
    cd = {}
    return render(request, 'www/copyright.html')

