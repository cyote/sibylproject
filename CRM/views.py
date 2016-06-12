# -*- coding: utf-8 -*-
from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponseRedirect, HttpResponse
from .models import Client, ClientFilter, Record, Appointment, Returning_call
from .forms import ClientForm, AppointmentForm, RecordForm, ClientEditForm, AppointmentEditForm, RecallForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import django_tables2 as tables



# Create your views here.
def index(request):
    return render(request, 'CRM/index.html', {})


def about(request):
    return render(request, 'CRM/about.html', {})



def client_list(request):
    clients = ClientFilter(request.GET, queryset=Client.objects.all())
    paginator = Paginator(clients, 5)
    page = request.GET.get('page')
    try:
        f = paginator.page(page)
    except PageNotAnInteger:
        f = paginator.page(1)
    except EmptyPage:
        f = paginator.page(paginator.num_pages)
    return render(request, 'CRM/client_list.html', {'f': f, 'page': page, 'clients': clients})


def client_detail(request, code):
    client = Client.objects.get(code=code)
    # 来访记录分页
    record_list = client.records.all().order_by('-created')
    record_paginator = Paginator(record_list, 5)
    record_page = request.GET.get('page')
    try:
        records = record_paginator.page(record_page)
    except PageNotAnInteger:
        records = record_paginator.page(1)
    except EmptyPage:
        records = record_paginator.page(record_paginator.num_pages)

    # 预约记录分页
    appointment_list = client.appointments.order_by('-date')
    app_paginator = Paginator(appointment_list, 5)
    app_page = request.GET.get('page')
    try:
        appointments = app_paginator.page(app_page)
    except PageNotAnInteger:
        appointments = app_paginator.page(1)
    except EmptyPage:
        appointments = app_paginator.page(app_paginator.num_pages)

    # 回访记录分页
    returning_calls_list = client.returning_calls.order_by('-created_date')
    rc_paginator = Paginator(returning_calls_list, 5)
    rc_page = request.GET.get('page')
    try:
        returning_calls = rc_paginator.page(rc_page)
    except PageNotAnInteger:
        returning_calls = rc_paginator.page(1)
    except EmptyPage:
        returning_calls = rc_paginator.page(rc_paginator.num_pages)

    # 添加回访
    if request.method == "POST":
        recallform = RecallForm(data=request.POST)

        if recallform.is_valid():
            new_recall = recallform.save(commit=False)
            new_recall.client = client
            new_recall.save()
        else:
            print(recallform.errors)
    else:
        recallform = RecallForm()

    return render(request, 'CRM/client_detail.html', {'client': client,
                                                      'records': records,
                                                      'appointments': appointments,
                                                      'returning_calls': returning_calls,
                                                      'recallform': recallform,
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


def edit_client(request, code):
    client = get_object_or_404(Client, code=code)

    if request.method == 'POST':
        editform = ClientEditForm(data=request.POST, instance=client)

        if editform.is_valid():
            editform.save(commit=True)
            messages.add_message(request, messages.SUCCESS, '修改成功')
            return client_detail(request, code)
        else:
            print(editform.errors)
    else:
        editform = ClientEditForm(instance=client)

    return render(request, 'CRM/edit_client.html', {'editform': editform})



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


def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        editform = AppointmentEditForm(data=request.POST, instance=appointment)

        if editform.is_valid():
            editform.save(commit=True)
            messages.add_message(request, messages.SUCCESS, '修改成功')
            return Appointment_list(request)
        else:
            print(editform.errors)
    else:
        editform = AppointmentEditForm(instance=appointment)

    return render(request, 'CRM/edit_appointment.html', {'editform': editform, 'appointment': appointment})


def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    messages.add_message(request, messages.SUCCESS, '已删除')
    return Appointment_list(request)


def records_list(request):
    record_list = get_list_or_404(Record)

    return render(request, 'CRM/records_list.html', {'record_list': record_list})


def records_detail(request, record_pk):
    record = get_object_or_404(Record, pk=record_pk)

    return render(request, 'CRM/records_detail.html', {'record': record})
