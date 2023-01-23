from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PhoneSerializer
from .models import Phone
# Create your views here.


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    permission_classes = []
    queryset = Phone.objects.all()