from django.db import models

class POST(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField()
    text = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    