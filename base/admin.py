from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

admin.site.register(User)
class roomAdmin(admin.ModelAdmin):
    list_display = ['host','topic','name', 'slug']
admin.site.register(Room,roomAdmin)
admin.site.register(Topic)
admin.site.register(Message)
