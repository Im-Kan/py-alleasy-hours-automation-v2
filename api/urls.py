from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.simple_response, name='simple_response'),
    path('convert/', views.convert, name='convert'),
    path('', views.home, name='home'),
]
