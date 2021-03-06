from django.contrib import admin

# Register your models here.
from .models import Customer,Job, GroupUser, TienSuBenh, News, Topic, NewPhotos, Datlichhen

admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(GroupUser)
admin.site.register(TienSuBenh)
admin.site.register(Datlichhen)

admin.site.register(Topic)

class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ("https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js","js/news.js",)
        # https://cdnjs.cloudflare.com/ajax/libs/tinymce/4.5.6/tinymce.min.js
admin.site.register(News, NewsAdmin)

class NewsFileAdmin(admin.StackedInline):
    model = NewPhotos

# @admin.register(News)
class CaseAdmin(admin.ModelAdmin):
    inlines = [NewsFileAdmin]

@admin.register(NewPhotos)
class NewsFileAdmin(admin.ModelAdmin):
    pass