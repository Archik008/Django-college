from django.shortcuts import render
from .models import ProductsModel

# Create your views here.

def render_shop(request):
    products = ProductsModel.objects.all()
    return render(request, "shop.html", {"products": products})

def about(request):
    return render(request, "about.html")