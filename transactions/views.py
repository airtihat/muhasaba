from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("مرحبًا بك في قسم الحركات المحاسبية")


