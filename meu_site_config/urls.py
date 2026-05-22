from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Adicione este import
from django.conf.urls.static import static # Adicione este import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
]

# Adicione estas linhas logo abaixo:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)