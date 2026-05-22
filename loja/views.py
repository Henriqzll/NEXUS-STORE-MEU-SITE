from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    # 1. Pega o termo digitado na barra de pesquisa
    search_query = request.GET.get('search_box', '')

    # 2. Se o usuário digitou algo, filtra os produtos pelo nome
    if search_query:
        products = Product.objects.filter(name__icontains=search_query).order_by('-created')
    else:
        # Se não houver pesquisa, traz todos os produtos ordenados pelos mais recentes
        products = Product.objects.all().order_by('-created')

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query
    }
    return render(request, 'store/index.html', context)


def product_detail(request, slug):
    # 3. Função para exibir o detalhe do produto (necessária para evitar o erro do terminal)
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)