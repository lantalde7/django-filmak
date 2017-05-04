from django.http import *
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from filmak.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from forms import LoginForm
from django.shortcuts import render

def sarrera(request):

	return render(request,'index.html', context_instance=RequestContext(request))
def logeatu(request):
	logout_bista(request)
	if request.POST:

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:

			login(request, user)
			izena=user.username
			return render(request,'logged/index.html', context_instance=RequestContext(request))
	return render(request,'login/index.html', context_instance=RequestContext(request))


def sortu_erabiltzailea(request):
	if request.POST:

		username = request.POST['username']
		password = request.POST['password']	

		user = authenticate(username=username, password=password)
		if user is None:
			tempUser=User.objects.create_user(username=username, password=password)	
			return render(request,'signup/succes.html', context_instance=RequestContext(request))
	
	return render(request,'signup/index.html', context_instance=RequestContext(request))

def logout_bista(request):
	logout(request)
	return render(request,'login/index.html', context_instance=RequestContext(request))