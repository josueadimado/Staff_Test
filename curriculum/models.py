from django.db import models

# Create your models here.
class Indicator(models.Model):
    code = models.CharField(max_length=5,null=True)
    name = models.CharField(max_length=50,null=True)
    question = models.CharField(max_length=100,null=True)


class IndicatorStatement(models.Model):
    indicator = models.ForeignKey(Indicator,null=True,on_delete=models.CASCADE,related_name="questions")
    statement = models.TextField(null=True)


# class Option(models.Model):
#     option = models.


