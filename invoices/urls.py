# invoices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='invoices_home'),
]
