# file like form
from rest_framework import serializers
from .models import Product,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class ProductSerializer(serializers.ModelSerializer):

    #category = CategorySerializer()
    #brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'