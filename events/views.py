from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from events.models import Event , Attendance
from events.forms import EventForm
from dateutil.parser import parse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect , Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import Event, Attendance
from events.forms import EventForm
#from django.contrib.auth import User

# LOGIN_URL
@login_required
def create(request):
	form  = EventForm(request.POST or None)
	if form.is_valid():
		event = form.save(commit = False)
		event.creator = request.user
		#event.creation_date = models.DateTimeField(default = datetime.now)  
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



	
	
	
	