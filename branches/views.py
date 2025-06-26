# branches/views.py

from django.http import HttpResponse

def branch_home(request):
    return HttpResponse("مرحبا بك في صفحة الفروع")

