# clients_suppliers/views.py

from django.shortcuts import render

def index(request):
    context = {
        "page_title": "العملاء والموردين"
    }
    return render(request, 'clients_suppliers/index.html', context)

def home_view(request):
    return render(request, 'home.html')