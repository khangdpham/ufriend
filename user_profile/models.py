from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class AppUserManager(BaseUserManager,PermissionsMixin):
    def create_user(self, username ,email,password=None):
		if not email:
			raise ValueError('User must have an email address')
		if not username:
			raise ValueError('User must have an valid username')
        user = self.model(username=username,email=self.normalize_email(email),)
        user.set_password(password)
		user.save(using-self._db)
        return user
 
    def create_superuser(self, email, synergy_level,
                         password):
        user = self.create_user(username=username, email = email,password=password)
        user.is_staff = True
		user.is_super_user = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumberica characters are allowed.')
	
	## Basic field
	username = models.CharField(max_length=254, unique=True)
	email = models.EmailField(blank=True) 
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active =  models.BooleanField(default=False,null=False)
	is_staff =  models.BooleanField(default=False,null=False)
	
	### Customized fields 
	group = models.CharField(max_length= 254, blank = True)
	#profile_image = models.ImageField(upload_to="upload",
	#	blank=False,null=False,
	#	default="/static/images/default.png")
	date_joined_epoch = models.IntegerField()
	location = models.CharField(max_length=254,blank = True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['email','username']
	
	def get_full_name(self):
		fullname = self.first_name+" "+self.last_name
		return fullname
	def get_short_name(self):
		return self.username
		
	def save(self,**kwargs):
		super(AppUser,self).save(**kwargs)
		
	objects = AppUserManager()
		