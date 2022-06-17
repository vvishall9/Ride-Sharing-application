from django.db import models
from django.contrib.auth.models import User


class Cities(models.Model):
    city = models.CharField(blank=False, null=False,
                            max_length=100, unique=True)
    distance = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.city


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=False, null=False,
                             max_length=100, unique=True)

    def __str__(self):
        return self.user.username
