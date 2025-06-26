from django.http import HttpResponse

def home(request):
    return HttpResponse("مرحباً بك في قسم العملاء.")
