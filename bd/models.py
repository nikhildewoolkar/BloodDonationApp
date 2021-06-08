from django.db import models
from django.contrib.auth.models import User,auth
from django.db.models.signals import *
from django.db.models.signals import post_save
class SignUp(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    bloodgroup=models.CharField(max_length=200)
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    def __str__(self):  # __str__
        return (self.user.username)
#def create_profile(sender, **kwargs):
#   if kwargs ['created']:
#        user = kwargs["instance"]
#        reg=UserProfile(user=user,usernames=user.username,phoneno="none",address="none",gender="other")
#        reg.save()
#        user_profile= UserProfile.objects.create(user=kwargs['instance'])
#post_save.connect(create_profile, sender=User, dispatch_uid="users-profilecreation-signal")
class Feedback(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=200)
    msg=models.CharField(max_length=500)

class advertise(models.Model):
    campname=models.CharField(max_length=100)
    campadd=models.CharField(max_length=200)
    campdate=models.CharField(max_length=100)
    camptime=models.CharField(max_length=100)
    regcontact=models.CharField(max_length=100)
