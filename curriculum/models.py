from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=20)

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
    document = models.FileField(upload_to="uploads/docs/",null=True,blank=True,blank=True)



