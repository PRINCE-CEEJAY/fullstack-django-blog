from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
