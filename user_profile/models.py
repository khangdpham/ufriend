from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class AppUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        user = self.model(email=email,)
        # <--snip-->
        return user
 
    def create_superuser(self, email, synergy_level,
                         password):
        user = self.create_user(email,password=password)
        user.is_super_user = True
        user.save()
        return user


class AppUser(AbstractBaseUser):
	username = models.CharField(max_length=254, unique=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(blank=True) 
	group = models.CharField(max_length= 254, blank = True)
	join_date = models.IntegerField()
	location = models.CharField(max_length=254,blank = True)
	is_active =  models.BooleanField(default=False)
	is_super_user = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	
		
	def save(self,**kwargs):
		super(AppUser,self).save(**kwargs)
		
	objects = AppUserManager()
		