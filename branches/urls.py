# branches/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.branch_home, name='branch_home'),
]
