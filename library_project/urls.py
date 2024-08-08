# library_project/urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from articles.views import custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', custom_login, name='login'),
    path('', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
