from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
import account
from account import urls
from categories.models import Categories
from main.forms import *
from main.utils import DataMixin


class MainHome(ListView):
    model = Categories
    form = SendEmail()
    template_name = 'main/index.html'
    context_object_name = 'category'


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'main/signin.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


    def get_success_url(self):
        return reverse_lazy('account')





