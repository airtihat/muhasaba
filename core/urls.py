# core/urls.py

from pathlib import Path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home  # ✅ استيراد صحيح
from django.http import HttpResponse
from .views import home_view

# تحديد BASE_DIR لاستخدامه مع static/media
BASE_DIR = Path(__file__).resolve().parent.parent

urlpatterns = [
    path('', home_view, name='home'),  # ✅ الصفحة الرئيسية من home.html
    path('admin/', admin.site.urls),

    # روابط التطبيقات
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

# دعم static/media في وضع التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "static")
    urlpatterns += static(settings.MEDIA_URL, document_root=BASE_DIR / "media")

# ✅ معالجة أخطاء مخصصة
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
