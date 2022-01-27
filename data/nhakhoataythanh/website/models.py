import email
from pickle import TRUE
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField(max_length=200)

class GroupUser(models.Model):
     name = models.TextField(max_length=200)

class TienSuBenh(models.Model):
    name = models.TextField(max_length=200, null=True)

class Customer(models.Model):
    code = models.CharField(max_length=200, null=True, unique=TRUE)
    name = models.CharField(max_length=200, null=True)
    # class gender(models.TextChoices):
    #     MAN = 'nam', _('Man')
    #     WOMAN = 'nu', _('Woman')
    GEN_CHOICES = (
    ("MAN", "Nam"),
    ("WOMAN", "Nữ"),
    )

    gender = models.CharField(max_length=9,
                  choices=GEN_CHOICES,
                  default="MAN")
    # gender = models.TextChoices('name':'Nam','nu':'Nữ')
    birthDay = models.DateField(null=True)
    address = models.TextField(max_length=500, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True)
    groupUser = models.ForeignKey(GroupUser, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    tienSuBenh = models.ForeignKey(TienSuBenh,on_delete=models.SET_NULL,null=True)
    tienSuBenhKhac = models.TextField(null=True)
    note = models.TextField(null=True)
