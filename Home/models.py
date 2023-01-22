from django.db import models


# Create your models here.
class UserCreds(models.Model):
    UserName = models.CharField(max_length=50)
    PassWord = models.CharField(max_length=50)

