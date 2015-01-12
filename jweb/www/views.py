from django.shortcuts import render
from django.template import RequestContext

from helpers import generate_breadcrumbs as gb

from www.models import Copyright, Home

def home(request):
    cd = {}
    cd = gb(cd, 'Home')
    cd['home_active'] = 'active'
    
    try:
        home = Home.objects.order_by('-updated_at')[0]
    except:
        home = Home()
        home.content = 'No home content, please add content.'
    cd['home'] = home
    
    return render(request, 'www/home.html', cd)

def copyright(request):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Copyright')
    cd['home_active'] = 'active'

    try:
        copy = Copyright.objects.order_by('-updated_at')[0]
    except:
        copy = Copyright()
        copy.content = 'No copyright content, please add content.'
    cd['copyright'] = copy
    
    return render(request, 'www/copyright.html', cd)

