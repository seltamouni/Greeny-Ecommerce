from django.urls import path
from .views import ProductList,ProductDetail,BrandList,BrandDetail,categoryList,test
from .api import ProductListAPI,ProductDetailAPI,BrandListAPI

app_name = 'products'

urlpatterns = [
    path('',ProductList.as_view(),name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view(), name='brand_list'),
    path('brands/<int:pk>', BrandDetail.as_view(), name='brand_detail'),
    path('category/', categoryList.as_view(), name='category_list'),
    path('testing/', test),
    #api
    # path('api/',product_list_api),
    # path('api/<int:id>', product_detail_api),
    
    #api class based view
    # path('api/cbv',ProductListAPI.as_view()),
    # path('api/cbv/<int:pk>', ProductDetailAPI.as_view()),

    path('api/', ProductListAPI.as_view()),
    path('api/<int:id>', ProductDetailAPI.as_view()),
    path('api/brands', BrandListAPI.as_view()),
]
