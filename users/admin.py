from django.contrib import admin
from . import models
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'passw']

admin.site.register(models.UserNames, CustomAdmin)