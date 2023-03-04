from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.account, name='account'),
    path('settings', views.settings, name='account_settings')
]

