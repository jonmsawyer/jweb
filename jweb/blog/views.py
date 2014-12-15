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
    return render(request, 'blog/home.html', cd)

def blog(request, slug):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')

    blog = Blog.objects.get(slug=slug)

    cd = gb(cd, blog.title, reverse('blog', slug=blog.slug))
    cd['blogs'] = list(blog)
    return render(request, 'blog/home.html', cd)

