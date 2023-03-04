from django.shortcuts import render
from django.views.generic import *
# Create your views here.


def account(request):
    return render(request, 'account/base_acc.html')


def settings(request):
    return render(request, 'account/account_settings.html')


