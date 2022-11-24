from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    fullname = models.CharField(max_length=150, blank=True, null=True, default='')
    username = models.CharField(max_length=150, unique=True, null=False)
    phone = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=False)
    confirm_password = models.CharField(max_length=50, null=False, default='SOME STRING')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'phone', 'password']

