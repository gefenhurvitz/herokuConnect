from django.db import models
from django.contrib.auth.models import User
 
 
class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
       return self.desc 


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    desc = models.CharField(max_length=50,null=True,blank=True)