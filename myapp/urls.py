from django.urls import path
from django.contrib import admin
from . import views
"""from django.contrib.auth import as auth_views"""
urlpatterns = [
    path('',views.home,name='home'),
    path('otp/<uid>', views.otpVerify, name='otp'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_acc,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('advice/',views.advice,name='advice'),
    path('doctors/',views.doctor,name='doctor'),
    path('payment/',views.payment,name='payment'),
    path('sucess/',views.sucess,name='sucess'),
]