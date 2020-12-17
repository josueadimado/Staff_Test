from django.contrib import admin
from .models import *


class StatementInline(admin.TabularInline):
    model = IndicatorStatement
    extra = 0
    

class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0

class IndicatorAdmin(admin.ModelAdmin):
    model = Indicator
    # inlines = [StatementInline,]

class StatementAdmin(admin.ModelAdmin):
    model = IndicatorStatement
    inlines = [ResourceInline,]  

class ResultSectionInline(admin.TabularInline):
    model = ResultSection
    readonly_fields = ['name','mean','sd']
    extra = 0
class ReviewSectionInline(admin.TabularInline):
    model = ReviewAnswer
    readonly_fields = ['question','answer','strength','indicator']
    extra = 0


class ResultAdmin(admin.ModelAdmin):
    model = Result
    inlines = [ResultSectionInline,ReviewSectionInline,]





   


# Register your models here.
admin.site.register(Section)
admin.site.register(Result,ResultAdmin)
admin.site.register(Indicator,IndicatorAdmin)
admin.site.register(IndicatorStatement,StatementAdmin)
