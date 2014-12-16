from django.conf.urls import patterns, include, url

from www import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^copyright/$', views.copyright, name='copyright'),
    url(r'^$', views.home, name='home'),
)

