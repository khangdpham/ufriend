from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class Event(models.Model):
	description = models.TextField()
	post_id = models.TextField(default='')
	title = models.TextField(default='')
	creation_date = models.DateTimeField(default = datetime.now)
	creator = models.ForeignKey(User,related_name='ev_creator_set')
	attendees = models.ManyToManyField(User, through='Attendance')
	latest = models.BooleanField(default=True)

	def save(self,**kwargs):
		super(Event,self).save(**kwargs)
		
	def __unicode__(self):
		return self.description
class Attendance(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)
	registration_date = models.DateTimeField(default = datetime.now)
	
	def __unicode__(self):
		return "%s is watching %s" (self.user.user_name , self.event)