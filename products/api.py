# views for api
from urllib import response
from .models import Product,Brand
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import generics

# @api_view(['GET'])
# def product_list_api(request):
#     objects = Product.objects.all()[:50]
#     data = ProductSerializer(objects,many=True).data
#     return Response({'status':200,'__all__':data})


# @api_view(['GET'])
# def product_detail_api(request,id):
#     objects = Product.objects.get(id=id)
#     data = ProductSerializer(objects).data
#     return Response({'status':200,'product detail':data})    


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   


class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer


class BrandListAPI(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

