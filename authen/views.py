from django.shortcuts import render_to_response
from django.contrib.auth import authenticate , login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect , Http404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authen.forms import UserCreateForm

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
	
def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/')
    else:
        #form = UserCreationForm()
        form = UserCreateForm()
    return render(request, "registration/register.html", {
        'form': form,

    })