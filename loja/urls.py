# No arquivo loja/urls.py

from django.urls import path
from . import views  # Isso importa todas as funções que estão dentro de views.py

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]