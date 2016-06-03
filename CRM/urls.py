__author__ = 'apple'
from django.conf.urls import patterns, url
from CRM import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^client_list/$', views.client_list, name='client_list'),
                       url(r'^client_list/client_detail/(?P<code>[0-9]{6})/$', views.client_detail,
                           name='client_detail'),
                       url(r'^add_client/$', views.add_client, name='add_client'),
                       url(r'^client_list/edit_client/(?P<code>[0-9]{6})/$', views.edit_client, name='edit_client'),
                       url(r'^appointment_list/$', views.Appointment_list, name='appointment_list'),
                       url(r'^appointment_list/edit_appointment/(?P<pk>[0-9]+)/$', views.edit_appointment,
                           name='edit_appointment'),
                       url(r'appointment_list/(?P<pk>[0-9]+)/delete/$', views.delete_appointment,
                           name='delete_appointment'),
                       url(r'^add_appointment/$', views.add_appointment, name='add_appointment'),
                       url(r'^records_list/$', views.records_list, name='records_list'),
                       url(r'^records_list/records_detail/(?P<record_pk>[0-9]+)/$', views.records_detail,
                           name='records_detail'),

                       )
