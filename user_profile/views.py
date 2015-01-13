from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login , views
from django.http import HttpResponseRedirect
 
def view_profile(request):
	username = request.user
	if request.user.is_authenticated():
		context = { 'username' : username , }
		return render_to_response(
			'profile/profile.html',
			context,
			context_instance=RequestContext(request))	
	else:	
		return HttpResponseRedirect('/login/')


