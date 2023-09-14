from typing import Any
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    subject = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    











