from django.shortcuts import render, get_list_or_404
from .models import Client

# Create your views here.
def index(request):
    return render(request, 'CRM/index.html', {})


def about(request):
    return render(request, 'CRM/about.html', {})


def client_list(request):
    client_list = get_list_or_404(Client, active=True)
    return render(request, 'CRM/client_list.html', {'client_list': client_list})
