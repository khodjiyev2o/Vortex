from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import OrderSerializer, CategorySerializer, UserSerializer, OrderSerializerForCategory
from .models import Order, Category






# @swagger_auto_schema(method='post', request_body=OrderSerializer, responses={201: OrderSerializer})


class CreateCategory(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class RetrieveDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateOrder(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class GetCategoryForOrder(generics.ListAPIView):
    serializer_class = OrderSerializerForCategory

    def get_object(self):
        pk = self.kwargs.get('pk')
        queryset = Category.objects.prefetch_related('orders').get(id=pk)
        return queryset
    
    def get_queryset(self):
        category = self.get_object()
        orders = category.orders.all()
        return orders

class ListUsers(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    queryset = User.objects.all()

       

class RetrieveUser(generics.RetrieveAPIView):
    authentication_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
