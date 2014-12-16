from django.conf.urls import patterns, include, url
from django.shortcuts import resolve_url, redirect
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jweb.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('www.urls')),
)
