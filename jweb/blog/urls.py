from django.conf.urls import patterns, include, url

from blog import views

urlpatterns = patterns('',
    # Examples:
    url(r'^page/(?P<page>\d+/)?$', views.home, name='blog_index_page'),
    url(r'^tag/(?P<tag>[a-z0-9-]+)/$', views.tag, name='tag_index'),
    url(r'^post/(?P<slug>[a-z0-9-]+)/$', views.blog, name='blog'),
    url(r'^$', views.home, name='blog_index'),
)

