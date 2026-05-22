from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}  # Preenche o slug automaticamente enquanto digita o nome

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category']
    list_filter = ['category']
    list_editable = ['price', 'stock']  # Permite editar preço e estoque direto pela lista
    prepopulated_fields = {'slug': ('name',)}

# Registros simples para monitorar os carrinhos e pedidos se quiser
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
