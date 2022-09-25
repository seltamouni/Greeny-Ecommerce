from django.contrib import admin
from .models import Profile,UserAddress,UserPhoneNumber

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserPhoneNumber)
admin.site.register(UserAddress)
