from django.contrib import admin

# Register your models here.
from .models import Customer,Job, GroupUser, TienSuBenh

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(GroupUser)
admin.site.register(TienSuBenh)
