__author__ = 'apple'
from django.conf.urls import patterns, url
from CRM import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),

                       )
