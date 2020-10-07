from django.contrib import admin
from .models import *


class CustomUserAdmin():
    pass

# Register your models here.
admin.site.register(CustomUserAdmin,CustomUser)

