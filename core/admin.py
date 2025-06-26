# core/admin.py
from django.contrib import admin
from clients_suppliers.models import Party

admin.site.register(Party)
