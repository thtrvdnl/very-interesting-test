from django.contrib.auth.models import User
from django.db import models

class Place(models.Model):
    """Keeping memories of visited places"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    comment = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location