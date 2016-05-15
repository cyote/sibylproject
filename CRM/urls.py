__author__ = 'apple'
from django.conf.urls import patterns, url
from CRM import views

app_name = 'CRM'
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^list/$', views.client_list, name='client_list')
                       )
