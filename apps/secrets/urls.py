from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^logout$', views.logout),
    url(r'^secret_post$', views.secret_post),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^like/(?P<id>\d+)$', views.like),
    url(r'^popular$', views.popular)
]
