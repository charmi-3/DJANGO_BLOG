from .views import *
from django.urls import path
from django.contrib.auth.views import *

urlpatterns = [
    path('signnin',LoginView.as_view(),name='login_page'),
    path('loggout',LogoutView.as_view(),name='logout_page'),
    path('signnup',Register.as_view(),name='signup_page')
]