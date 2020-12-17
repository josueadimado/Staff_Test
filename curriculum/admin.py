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


class ResultAdmin(admin.ModelAdmin):
    model = Result
    inlines = [ResultSectionInline,]

class ReviewSectionInline(admin.TabularInline):
    model = ReviewAnswer
#     readonly_fields = ['name','mean','sd']
    extra = 0


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    inlines = [ReviewSectionInline,]


# Register your models here.
admin.site.register(Section)
admin.site.register(Result,ResultAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Indicator,IndicatorAdmin)
admin.site.register(IndicatorStatement,StatementAdmin)
