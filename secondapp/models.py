from django.db import models

# Create your models here.
class Dest(models.Model):
    img = models.ImageField(upload_to='static')
    nameimg1 = models.CharField(max_length=20)
    
class Message(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    img1= models.ImageField(upload_to='pic')
    
class Service(models.Model):
    title1 = models.CharField(max_length=20)
    description1 = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    number = models.CharField(max_length=100)
    message = models.TextField()

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")