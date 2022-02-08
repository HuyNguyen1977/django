from django.contrib import admin

# Register your models here.
from .models import Customer,Job, GroupUser, TienSuBenh, News, Topic

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(GroupUser)
admin.site.register(TienSuBenh)
admin.site.register(News)
admin.site.register(Topic)
