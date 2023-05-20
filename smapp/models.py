from random import choices
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name ='user'
        verbose_name_plural='users'
        db_table='user'
    email = models.EmailField(('email address'), unique=True,blank=True)
    username=models.CharField(max_length=15,unique=True,blank=True)
    fullname=models.CharField(max_length=30,blank=True)
    gender=models.CharField(max_length=10,blank=True)
    mobile_no=models.CharField(max_length=10,blank=True)
    photo=models.ImageField(upload_to = "photos",max_length=200,null=True)
    role=models.CharField(max_length=10,blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class product(models.Model):
    prod_name=models.CharField(max_length=30,blank=False)
    prod_sku=models.CharField(max_length=10,blank=False)
    prod_price=models.IntegerField(blank=True)
    prod_quantity=models.IntegerField(blank=True)
    prod_image=models.ImageField(upload_to="photos",max_length=200,null=True)
    items_bought=models.IntegerField(blank=True,default=0)

    class Meta:
        db_table='product'

class retailerData(models.Model):
    ret_name=models.CharField(max_length=30,blank=False)
    p_sku=models.CharField(max_length=10,blank=False)
    p_name=models.CharField(max_length=30,blank=False)
    p_quantity=models.IntegerField(blank=True)
    date=models.CharField(max_length=20,blank=True)

    class Meta:
        db_table='retailerData'