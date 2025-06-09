from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    age = models.IntegerField(default=0)
    reference = models.CharField(max_length=20, null=True)


class Email(models.Model):

    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email
