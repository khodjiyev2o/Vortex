from django.db import models
from django.contrib.auth.models import User
from stores.models import Store
# Create your models here.

STATUS_CHOICES = [
        ('is_owner', 'Owner'),
        ('is_staff', 'Staff'),
        ('is_courier', 'Courier')
    ]

class Profile(User):
    profile_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    profile_photo = models.FileField(null=True,blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    