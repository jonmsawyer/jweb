from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from helpers import generate_breadcrumbs as gb

from blog.models import Blog


def home(request, page=1):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')
    
    blogs_list = Blog.objects.order_by('-created_at')
    paginator = Paginator(blogs_list, 10) # Show 25 blogs per page
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    for blog in blogs:
        blog.list_tags = blog.tags.split()
        try:
            blog.preview = ''.join(blog.content.split('<!--preview-->')[1]).split('<!--/preview-->')[0]
        except IndexError:
            blog.preview = blog.content
    
    cd['blogs'] = blogs
    cd['page_range'] = paginator.page_range
    cd['current_page_num'] = blogs.number
    cd['blog_active'] = 'active'
    
    return render(request, 'blog/home.html', cd)

def blog(request, slug):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')
    
    blog = Blog.objects.get(slug=slug)
    blog.list_tags = blog.tags.split()
    
    cd['blog_active'] = 'active'
    cd['blogs'] = (blog,)

    return render(request, 'blog/blog.html', cd)

def tag(request, tag):
    cd = {}
    cd = gb(cd, 'Home')
    cd = gb(cd, 'Blog', name='blog_index')
    cd = gb(cd, 'Tag', name='tag_index')

    if tag:
        blogs_list = Blog.objects.filter(tags__contains=tag).order_by('-created_at')
    else:
        blogs_list = Blog.objects.order_by('-created_at')

    cd['blogs'] = blogs_list
    cd['blog_active'] = 'active'

    return render(request, 'blog/home.html', cd)
