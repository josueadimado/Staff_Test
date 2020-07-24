from django.contrib import admin
from .models import *


class StatementInline(admin.TabularInline):
    model = IndicatorStatement
    extra = 0

class IndicatorAdmin(admin.ModelAdmin):
    model = Indicator
    inlines = [StatementInline,]


# Register your models here.
admin.site.register(Indicator,IndicatorAdmin)
