from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now=True)
    
