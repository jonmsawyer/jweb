from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    # Examples:
    url(r'(?P<slug>[a-z0-9-]+)', views.blog, name='blog'),
    url('', views.home, name='blog_index'),
)

