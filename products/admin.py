from django.contrib import admin
from .models import Product,Brand,Category,ProductImages,ProductReview
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

#display products : some cullomn
# it helps to add images in the same time we create the product
class ProductImageInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name','price','flag']#only this colums appear in the list of products 
    inlines = [ProductImageInline]#it helps to add images in the same time we create the product


    
    


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductReview)
admin.site.register(ProductImages)