from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your models here.


class RegUser(User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class Dog(models.Model):
    name = models.CharField(max_length=40)
    bday = models.DateField()
    owner = models.ForeignKey(User, related_name='dogs', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('dogs_cats:list_dog')

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField(max_length=40)
    bday = models.DateField()
    owner = models.ForeignKey(User, related_name='cats', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('dogs_cats:list_cat')

    def __str__(self):
        return self.name
