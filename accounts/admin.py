from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.
admin.site.register(CustomUserAdmin,CustomUser)

