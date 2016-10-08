"""
Definition of urls for MusicStore.
"""
from django.contrib.auth.views import login, logout
from datetime import datetime
from django.contrib import admin
from django.conf.urls import url, include
from app.forms import BootstrapAuthenticationForm
from app.views import home, contact, about
urlpatterns =[
    # Examples:
    url(r'^artists$', include('app.urls')),
    #url(r'^artists$', artists, name='artists'),
    #url(r'^artists/create$', artistcreate, name='artistcreate'),
    #url(r'^artists/(?P<id>\d+)$',artistdetails, name='artistdetails'),
    ##url(r'^artists/(?P<name>[A-Za-z]+)$', 'app.views.artistdetails', name='artistdetails'),

    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),

    url(r'^login/$', login, { 'template_name': 'app/login.html',
                              'authentication_form': BootstrapAuthenticationForm,
                              'extra_context':  { 'title':'Log in', 'year':datetime.now().year, }
                            },
        name='login'),
    url(r'^logout$', logout, {'next_page': '/', }, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
