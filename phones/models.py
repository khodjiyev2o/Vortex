from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ('on_road', 'On Road'),
        ('active', 'Active'),
        ('sold', 'Sold')
    ]

class Phone(models.Model):
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    

    def __str__(self):
        return self.model