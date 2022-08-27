from itertools import product
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductList(ListView):
    model = Product