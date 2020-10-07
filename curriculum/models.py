from django.db import models
from django.conf import settings

class Section(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

# Create your models here.
class Indicator(models.Model):
    section = models.ForeignKey(Section,null=True,on_delete=models.CASCADE,related_name="indicators")
    code = models.CharField(max_length=5,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    question = models.CharField(max_length=500,null=True,blank=True)
    resource_title = models.CharField(max_length=500,null=True,blank=True)
    resource_document = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.code)+" : "+str(self.name)
 

class IndicatorStatement(models.Model):
    indicator = models.ForeignKey(Indicator,null=True,on_delete=models.CASCADE,related_name="questions")
    statement = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.indicator.code)+" : "+str(self.statement)



class Resource(models.Model):
    statement = models.ForeignKey(IndicatorStatement,null=True,on_delete=models.CASCADE,related_name="resources")
    title = models.CharField(max_length=100,null=True,blank=True)
    document = models.FileField(upload_to="uploads/docs/",null=True,blank=True)

class Result(models.Model):
    institution = models.CharField(max_length=100,null=True)
    comment = models.TextField(null=True)
    taker = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)


class ResultSection(models.Model):
    name = models.CharField(max_length=50,null=True)
    mean = models.FloatField(default=1.0)
    sd = models.FloatField(default=0.0)
    # indicator = models.ForeignKey(Indicator,null=True,on_delete=models.CASCADE,related_name="results")
    result = models.ForeignKey(Result,null=True,on_delete=models.CASCADE,related_name="results")
    

    def __str__(self):
        return "Mean of "+str(self.mean)+" and S.D of "+str(self.sd)

