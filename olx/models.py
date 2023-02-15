from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.ImageField(null=True,upload_to="profile.images")
    address=models.CharField(max_length=300)
    phone=models.PositiveIntegerField()

    
  
class Products(models.Model):

    CONDITION__CHOICES=(
         ('SPORTS','SPORTS'),
         ('FURNITURES','FURNITURES'),
         ('ELECTRONICS','ELECTRONICS'),
         ('MOBILES','MOBILES'),
         ('OTHERS','OTHERS')
    )
    
    
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=500)
    condition=models.CharField(max_length=200)
    category=models.CharField(max_length=20,choices=CONDITION__CHOICES)
    photo=models.ImageField(upload_to='product_photos',null=True,blank=True)
    location=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    updated_at=models.DateTimeField(auto_now=True)
    
    
    Options=(
        ("for-sale","for-sale"),
        ("exchange","exchange"),
        ("rent","rent")
    )
    status=models.CharField(max_length=30, choices=Options,default="for-sale")
    created_date=models.DateField(auto_now_add=True)
    


    


class Brand(models.Model):
    brand_name=models.CharField(max_length=100)




class Notifications(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    Options=(
        ("sent","sent"),
        ("pending","pending"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=50,choices=Options)






