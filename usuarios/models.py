from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    picture = models.ImageField(default='avatar.png', upload_to='users/')

