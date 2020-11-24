from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100,null=True,blank=True)
    recover_token = models.CharField(max_length=60,null=True,blank=True)
    
class Email(models.Model):
    subject = models.CharField(max_length=200,default='VVU Mail')
    text = models.TextField(null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    received = models.BooleanField(default=False)
    recepients = models.ManyToManyField(CustomUser,blank=True,related_name="recepients")#,default=CustomUser.objects.filter(subscribed_to_mail=True))


    def __str__(self):
        return self.subject
