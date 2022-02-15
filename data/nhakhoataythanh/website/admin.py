from django.contrib import admin

# Register your models here.
from .models import Customer,Job, GroupUser, TienSuBenh, News, Topic

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(GroupUser)
admin.site.register(TienSuBenh)

admin.site.register(Topic)

class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ("https://cdnjs.cloudflare.com/ajax/libs/tinymce/4.5.6/tinymce.min.js","js/news.js",)
admin.site.register(News, NewsAdmin)