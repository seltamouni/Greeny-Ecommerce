from itertools import product
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,ProductImages
# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImages.objects.filter(product=myproduct)
        return context
       