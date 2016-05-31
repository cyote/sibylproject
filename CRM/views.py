# -*- coding: utf-8 -*-
from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Client, Record, Appointment, Returning_call
from .forms import ClientForm, AppointmentForm, RecordForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django import forms

# Create your views here.
def index(request):
    return render(request, 'CRM/index.html', {})


def about(request):
    return render(request, 'CRM/about.html', {})


def client_list(request):
    client_list = get_list_or_404(Client, active=True)
    return render(request, 'CRM/client_list.html', {'client_list': client_list})


def client_detail(request, code):
    client = Client.objects.get(code=code)

    records = client.records.all().order_by('-created')
    appointments = client.appointments.order_by('-date')
    returning_calls = client.returning_calls.order_by('-created_date')

    return render(request, 'CRM/client_detail.html', {'client': client,
                                                      'records': records,
                                                      'appointments': appointments,
                                                      'returning_calls': returning_calls
                                                      })


def add_client(request):
    if request.method == 'POST':
        client_form = ClientForm(data=request.POST)

        if client_form.is_valid():
            client_form.save(commit=True)
            # return client_list(request)
            messages.add_message(request, messages.SUCCESS, '创建成功')
            return HttpResponseRedirect(reverse_lazy('client_list'))

        else:
            print(client_form.errors)
    else:
        client_form = ClientForm()

    return render(request, 'CRM/add_client.html', {'client_form': client_form})


def Appointment_list(request):
    list = get_list_or_404(Appointment)

    return render(request, 'CRM/appointment.html', {'list': list})


def add_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(data=request.POST)

        if appointment_form.is_valid():
            appointment_form.save(commit=True)
            # return HttpResponseRedirect(reverse_lazy('Appointment_list'))
            messages.add_message(request, messages.SUCCESS, '创建成功')
            return Appointment_list(request)
        else:
            print(appointment_form.errors)
    else:
        appointment_form = AppointmentForm()

    return render(request, 'CRM/add_appointment.html', {'appointment_form': appointment_form})


def records_list(request):
    record_list = get_list_or_404(Record)

    return render(request, 'CRM/records_list.html', {'record_list': record_list})


def records_detail(request, record_pk):
    record = get_object_or_404(Record, pk=record_pk)

    return render(request, 'CRM/records_detail.html', {'record': record})
