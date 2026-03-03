from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)