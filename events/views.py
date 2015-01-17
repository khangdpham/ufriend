from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from events.models import Event , Attendance
from events.forms import EventForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect , Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import Event, Attendance
from events.forms import EventForm
import hashlib ,time

#from django.contrib.auth import User

SALT='this is secret salt and pepper'

# LOGIN_URL
@login_required
def create(request):
	form  = EventForm(request.POST or None)
	if form.is_valid():
		event = form.save(commit = False)
		event.creator = request.user
		#event.post_id = md5.new(event.creator+SALT+calendar.timegm())
		event.post_id = hashlib.sha224(str(event.creator)+SALT+str((int(time.time())))).hexdigest()
		event.save()
		messages.success(request,'Successfully posted')
		if 'next' in request.POST:
			next = request.POST['next']
		else:
			next = reverse('home')
		return HttpResponseRedirect(next)
	''' If not POST 
		render to FORM 
	'''
	context = {'username': request.user,'forms':EventForm,}
	return render(request,'events/create.html',context)

def display_current_events(request):
	events = Event.objects.all()
	context = { 'events' : events }
	
	return render(request,'events/current_events.html',context)
	
def view_event(request,event_id):
	event = Event.objects.all().filter(post_id=event_id)
	context = { 'event':event ,}
	return render(request,'events/view.html',context)
		

	
	
	
	
	
	
	
	

	
	
	
	
