from django.db import models

# Create your models here.
class Indicator(models.Model):
    code = models.CharField(max_length=5,null=True)
    name = models.CharField(max_length=100,null=True)
    question = models.CharField(max_length=500,null=True)
    resource_title = models.CharField(max_length=500,null=True)
    resource_document = models.TextField(null=True)

    def __str__(self):
        return str(self.code)+" : "+str(self.name)
 

class IndicatorStatement(models.Model):
    indicator = models.ForeignKey(Indicator,null=True,on_delete=models.CASCADE,related_name="questions")
    statement = models.TextField(null=True)

    def __str__(self):
        return str(self.indicator.code)+" : "+str(self.statement)



class Resource(models.Model):
    statement = models.ForeignKey(IndicatorStatement,null=True,on_delete=models.CASCADE,related_name="resources")
    title = models.CharField(max_length=100,null=True)
    document = models.FileField(upload_to="uploads/docs/",null=True,blank=True)



