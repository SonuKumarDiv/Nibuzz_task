from django.db import models


class User(models.Model):
    email=models.EmailField(max_length=60, unique=True)
    username=models.CharField(max_length=30,default='',unique=True)
    signup_date=models.DateTimeField()
	

class User_profile(models.Model):
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='User')
    user_type= models.CharField(max_length=12,default='User')
    profile_pic=models.ImageField(upload_to='user/profile_image',default='deafult_profile_pic.jpeg')
    country_code=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)
    address=models.CharField(max_length=15)
