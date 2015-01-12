from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<slug>[a-z0-9-]+)/$', views.blog, name='blog'),
    url(r'^page/(?P<page>\d+)/$', views.home, name='blog_index_page'),
    url(r'^$', views.home, name='blog_index'),
)

