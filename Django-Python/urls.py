from django.conf.urls import patterns, include, url
from django.contrib import admin
from employees import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django-Python.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Separating the admin site from the user site with respect url patterns
    url(r'^', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
)
