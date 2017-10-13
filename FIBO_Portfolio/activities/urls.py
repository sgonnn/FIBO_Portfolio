from django.conf.urls import url
from . import views

urlpatterns = [
    #/activities/
    url(r'^$', views.index, name='index'),
    #/activities/create
    url(r'^create$', views.createActivity, name='createActivity')
]
