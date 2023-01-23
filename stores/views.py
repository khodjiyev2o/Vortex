from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StoreSerializer
from .models import Store
# Create your views here.


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = []
    queryset = Store.objects.all()