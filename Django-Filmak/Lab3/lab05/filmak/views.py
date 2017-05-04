from django.http import *
from django.shortcuts import render_to_response,redirect,render,get_object_or_404
from django.template import RequestContext
from filmak.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from forms import LoginForm
from django.shortcuts import render

def sarrera(request):
	filmak_lista=Filma.objects.all()
	return render(request,'index.html', {'filmak_lista':filmak_lista},context_instance=RequestContext(request) )
def logeatu(request):
	logout_bista(request)
	if request.POST:

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:

			login(request, user)
			izena=user.username
			return render(request,'logged/index.html',{'erabiltzailea':user}, context_instance=RequestContext(request))
	return render(request,'login/index.html',  context_instance=RequestContext(request))


def sortu_erabiltzailea(request):
	if request.POST:

		username = request.POST['username']
		password = request.POST['password']	

		user = authenticate(username=username, password=password)
		if user is None:
			tempUser=User.objects.create_user(username=username, password=password)	
			return render(request,'signup/succes.html', context_instance=RequestContext(request))
		else:
			raise forms.ValidationError("kk")			
	
	return render(request,'signup/index.html', context_instance=RequestContext(request))

def logout_bista(request):
	erabiltzailea=request.user
	logout(request)
	return render(request,'logout/index.html', {'erabiltzailea':erabiltzailea},context_instance=RequestContext(request))

def bozkatzaileak(request, filmaId):
	if request.user.is_anonymous():
		return render(request,'errors/logerror.html', context_instance=RequestContext(request))
	filma=Filma.objects.get(pk=filmaId)
	erabiltzaileak=filma.bozkatzailea_set.all()
		
		
	return render(request,'bozkatzaileak/index.html', {'erabiltzaileak':erabiltzaileak,'filma':filma},context_instance=RequestContext(request))

def logged(request):
	filmak_lista=Filma.objects.all()
	if request.user.is_anonymous():
		return render(request,'errors/logerror.html', context_instance=RequestContext(request))

	return render(request,'filmak/index.html',  {'filmak_lista':filmak_lista}, context_instance=RequestContext(request))
def bozkatu(request):
	if not request.user.is_anonymous():
		aukerak=[]
		if request.POST:
			bozka_lista=request.POST.getlist('fl')
			print bozka_lista
			
			for fid in bozka_lista:
				aukera=Filma.objects.get(pk=fid)
				aukera.bozkak +=1
				aukerak.append(aukera)
				aukera.save()
				if not request.user.is_anonymous():
					erab=request.user
					try:
						bozkatzaile=Bozkatzailea()
						bozkatzaile=Bozkatzailea.objects.get(erabiltzailea_id=erab.pk)
					except bozkatzaile.DoesNotExist:
						bozkatzaile=Bozkatzailea(erabiltzailea=erab)
						bozkatzaile.save()
				bozkatzaile.gogoko_filmak.add(aukera)
	if request.user.is_anonymous():
		return render(request,'errors/logerror.html', context_instance=RequestContext(request))

	return render(request,'bozkatuta/index.html', {'bozka_lista':aukerak},context_instance=RequestContext(request))


