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


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(), label='预约日期')

    class Meta:
        model = Appointment
        fields = ['client', 'time_slot', 'date', 'subject', 'comment']
