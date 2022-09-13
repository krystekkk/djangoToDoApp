from django.db import models
from django.contrib.auth.models import User


class Todos(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
