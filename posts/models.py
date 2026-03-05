from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Post, on_delete=models.CASCADE)
