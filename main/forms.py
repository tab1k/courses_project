from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from main.models import *

class SendEmail(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'})),
    password1= forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'input'})),
    password2 = forms.CharField(label='Повторите пароль', widget=forms.TextInput(attrs={'class': 'input'})),

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input'})),
    password= forms.CharField(label='Пароль', widget=forms.TextInput(attrs={'class': 'input'}))