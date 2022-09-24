from itertools import product
from msilib.schema import ListView
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Brand, Product,ProductImages,Category
from django.db.models import Count,Q,F
# Create your views here.

class ProductList(ListView):
    model = Product
    #html:product_list;object_list
    #context:product_list;object_list
    paginate_by=100

class ProductDetail(DetailView):
    model = Product 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()#return the actual object
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)
        return context
       
class BrandList(ListView):
    model = Brand  
    #paginate_by = 5 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands']=Brand.objects.all().annotate(product_count=Count('product_brand'))
        return context   

class BrandDetail(DetailView):
    model = Brand
    #paginate_by = 10
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand= brand)
        return context

class categoryList(ListView):
    model = Category
    paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all().annotate(
            product_count=Count('product_category'))
        return context
                

def test(request):
    #context = Product.objects.filter(name__contains='sara')
    #context = Product.objects.order_by('name')
    #context = Product.objects.all()[:15]
    #context = Product.objects.values('id','name','sku')
    context = Product.objects.values('id','name','price')
    return render (request,'products/test_list.html',{'products':context})                