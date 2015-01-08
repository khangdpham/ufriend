from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login

def index(request):
	username = request.user
	context = {'state':'','username':username, }
	return render_to_response('home/index.html',
		context,
		context_instance = RequestContext(request),
	)
