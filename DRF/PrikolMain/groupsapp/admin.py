from django.contrib import admin

from .models import *

from django.contrib.auth.models import User


# Register your models here.


class MyGroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'countOfMembers', 'time_create', 'is_open')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(MyGroups,MyGroupsAdmin)

admin.site.register(Goods)

admin.site.register(Profile)
