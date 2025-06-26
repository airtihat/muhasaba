# clients_suppliers/urls.py

from django.urls import path
from . import views  # ← هذا السطر يسبب الخطأ إن لم يوجد views.py

urlpatterns = [
    path('', views.index, name='clients_suppliers_home'),
]
