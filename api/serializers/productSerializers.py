from api.models import Category, Product, Review
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'description', 'price', 'stock', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'product', 'user', 'ratings', 'created_at', 'updated_at']


