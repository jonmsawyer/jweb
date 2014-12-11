from django.shortcuts import render
from django.template import RequestContext

from helpers import generate_breadcrumbs as gb

def home(request):
    cd = {}
    cd = gb(cd, 'Home')
    return render(request, 'www/home.html', cd)

def copyright(request):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Copyright')
    return render(request, 'www/copyright.html', cd)

