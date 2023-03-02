
from django.urls import path
from main import views
from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('signin', RegisterUser.as_view(), name='signin'),

]

