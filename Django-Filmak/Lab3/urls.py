from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView,CreateView
from filmak.models import Filma,Bozkatzailea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


urlpatterns = patterns('',
		url(r'^$', 'filmak.views.sarrera'),
	    url(r'^filmaktaula/$',
	        ListView.as_view(
	            queryset=Filma.objects.all(),
	            context_object_name='filmak_list',
	            template_name='filmak/index.html')),
	    url(r'^filmaktaula/bozkatzaileak/$',
	        DetailView.as_view(
	            model=Filma,
	            template_name='index.html')),
		url(r'^filmaktaula/(?P<pk>\d+)/$',
	        DetailView.as_view(
	            model=Filma,
	            template_name='filmak/filmak_details.html')),
		url(r'^login/$','filmak.views.logeatu'),
		#url(r'^signup/$',
	      # 'django.contrib.auth.views.login', {'template_name': 'signup/index.html'}),

		url(r'^signup/$', 'filmak.views.sortu_erabiltzailea'),


)