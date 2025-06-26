# core/urls.py

from pathlib import Path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

# 🧠 استيراد views بشكل آمن مع بدائل افتراضية أثناء التطوير
try:
    from core.views import home, page_not_found, server_error
except ImportError:
    home = lambda request: HttpResponse("الصفحة الرئيسية غير مفعّلة بعد")
    page_not_found = server_error = None

# تحديد BASE_DIR لاستخدامه مع static/media
BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('', home, name='home'),  # ✅ الصفحة الرئيسية
    path('admin/', admin.site.urls),

    # ✅ روابط التطبيقات
    path('accounts/', include('accounts.urls')),
    path('branches/', include('branches.urls')),
    path('clients/', include('clients.urls')),
    path('clients-suppliers/', include('clients_suppliers.urls')),
    path('expenses/', include('expenses.urls')),
    path('invoices/', include('invoices.urls')),
    path('journals/', include('journals.urls')),
    path('reports/', include('reports.urls')),
    path('transactions/', include('transactions.urls')),
    path('users/', include('users.urls')),
]

# ✅ دعم ملفات static و media فقط أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")
    urlpatterns += static(settings.MEDIA_URL, document_root=BASE_DIR / "media")

# ✅ معالجات مخصصة للأخطاء
if page_not_found:
    handler404 = 'core.views.page_not_found'
if server_error:
    handler500 = 'core.views.server_error'


def home_view(request):
    return render(request, 'home.html')

def page_not_found(request, exception=None):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)