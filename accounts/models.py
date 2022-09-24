from distutils.command.upload import upload
from random import choices
from django.db import models
from django_countries.fields import Country_Field
from django.contrib.auth.models import User
from utils.generate_code import generate_code

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users')

    code = models.CharField(max_length=10,default=generate_code)
    code_used = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

DATA_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Academy','Academy'),
    ('Other','Other'),
)    

class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    type = models.CharField(choices=DATA_TYPE,max_length=10)


class UserAddress(models.Model):
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(choices=DATA_TYPE, max_length=10)
    country = Country_Field()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    street = models.CharField(max_length=80)
    notes = models.CharField(max_length=200)

