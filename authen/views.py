from django.shortcuts import render_to_response
from django.contrib.auth import authenticate , login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect , Http404


def login_user(request):
	state = "Please log in :"
	username = password = ''
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username , password= password)
		if user is not None:
			if user.is_active:
				login(request,user)
				state = ' You are successfully logged in'
			else:
				state = " Inactive account "
		else:
			state = " Invalid login "
		if 'next' in request.POST:
			next = request.POST['next']
		else:
			next = reverse('home.views.index')
		return HttpResponseRedirect(next)
	return render_to_response('authen.html',{'state':state,'username':username})