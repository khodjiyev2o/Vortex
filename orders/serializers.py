from rest_framework import serializers
from .models import Order, Category
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class OrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    class Meta:
        model = Order
        fields  = ['id', 'cost', 'category']

class OrderSerializerForCategory(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields  = ['id','user', 'cost']

    def create(self, validated_data):
        category = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category)
        validated_data['category'] = category
        validated_data['user'] = User.objects.get(id=1)
        order = Order.objects.create(**validated_data)
        return order    