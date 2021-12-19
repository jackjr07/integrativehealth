from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.healthlitIndex, name='healthlit'),
    path('sub/', views.subprogramIndex, name='subhealthlit'),
    
]

