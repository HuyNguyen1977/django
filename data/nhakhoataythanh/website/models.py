import email
from email.mime import image
from pickle import TRUE
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.template.defaultfilters import slugify

# Create your models here.
# class User(AbstractUser):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)
#     avatar = models.ImageField(null=True, default="avatar.svg")

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class GroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    def __str__(self):
        return self.name

class TienSuBenh(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200, null=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
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

class News(models.Model):
    id = models.AutoField(primary_key=True)
    userPost = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # slug = models.SlugField(null=False, default=uuid.uuid1)
    slug = models.SlugField(max_length=200, db_index=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    # description = HTMLField(null=True, blank=True)
    description = models.TextField(null=True)
    # participants = models.ManyToManyField( User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class NewPhotos(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='news/')