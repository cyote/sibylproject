__author__ = 'apple'
# -*- coding: utf-8 -*-
from .models import Client, Appointment, Record, Returning_call
from django import forms
from django.forms.extras import SelectDateWidget
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from datetime import datetime


class ClientForm(forms.ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget(years=range(date.today().year - 60, date.today().year)),
                               label='出生日期')

    class Meta:
        model = Client
        exclude = ['code', 'created', 'updated']


class ClientEditForm(forms.ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget(years=range(date.today().year - 60, date.today().year)),
                                   label='出生日期')

    class Meta:
        model = Client
        exclude = ['code', 'created', 'updated']


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(), label='预约日期')

    class Meta:
        model = Appointment
        fields = ['client', 'time_slot', 'date', 'subject', 'comment']


class AppointmentEditForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(), label='预约日期')

    class Meta:
        model = Appointment
        fields = ['time_slot', 'date', 'subject', 'confirm_status', 'comment']


class RecordForm(forms.ModelForm):
    appointment = Appointment.objects.filter(confirm_status='co')

    class Meta:
        model = Record
        exclude = ['created', 'updated']


class RecallForm(forms.ModelForm):
    call_date = forms.DateField(widget=SelectDateWidget(), label='回访日期')

    class Meta:
        model = Returning_call
        fields = ('call_date', 'comment')
