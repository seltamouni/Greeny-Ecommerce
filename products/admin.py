from django.contrib import admin
from .models import Product,Brand,Category,ProductImages,ProductReview

# Register your models here.

#display products some cullomn
class ProductImageInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','flag']
    inlines = [ProductImageInline]
    


admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductReview)
admin.site.register(ProductImages)