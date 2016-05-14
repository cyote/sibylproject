from django.shortcuts import render

# Create your views here.
def index(request):
    hail = "你好"
    return render(request, 'CRM/base.html', {'hail': hail})