from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.vascularBridge, name='vascularBridge'),        
    path('register',views.vascularBridgeRegister, name='vascularBridgeRegister'),
]
