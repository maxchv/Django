from django.conf.urls import url

from .views import artists, artistcreate, artistdetails

urlpatterns = [
    url(r'^$', artists, name='artists'),
    url(r'^create$', artistcreate, name='artistcreate'),
    url(r'^(?P<id>\d+)$', artistdetails, name='artistdetails'),
    #url(r'^artists/(?P<name>[A-Za-z]+)$', 'app.views.artistdetails', name='artistdetails'),
]