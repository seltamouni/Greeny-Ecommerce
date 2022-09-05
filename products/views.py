from itertools import product
from msilib.schema import ListView
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,ProductImages
# Create your views here.

class ProductList(ListView):
    model = Product
    #html:product_list;object_list
    #context:product_list;object_list

class ProductDetail(DetailView):
    model = Product 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()#return the actual object
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)
        return context
       