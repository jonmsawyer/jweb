from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse

from helpers import generate_breadcrumbs as gb

from blog.models import Blog


def home(request):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')
    cd['blogs'] = Blog.objects.all()
    for blog in cd['blogs']:
        blog.list_tags = blog.tags.split()
    cd['blog_active'] = 'active'
    return render(request, 'blog/home.html', cd)

def blog(request, slug):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')

    blog = Blog.objects.get(slug=slug)

    #cd = gb(cd, blog.title, reverse('blog', blog.slug))
    cd['blogs'] = (blog,)
    for blog in cd['blogs']:
        blog.list_tags = blog.tags.split()
    cd['blog_active'] = 'active'
    return render(request, 'blog/home.html', cd)

