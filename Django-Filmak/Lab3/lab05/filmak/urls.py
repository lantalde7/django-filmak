from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView,CreateView
from filmak.models import Filma,Bozkatzailea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
		url(r'^$', 'filmak.views.sarrera'),
		url(r'^logged/$','filmak.views.logged'),
	    url(r'^filmaktaula/$',login_required(
	        ListView.as_view(
	            queryset=Filma.objects.all(),
	            context_object_name='filmak_list',
	            template_name='filmak/index.html'))),
	    url(r'^logged/(?P<pk>\d+)/$',
	        DetailView.as_view(
	            model=Filma,
	            template_name='filmak/filmak_details_logged.html')),
	    url(r'^bozkatuta/$',
	        'filmak.views.bozkatu'),
	    url(r'^bozkatzaileak/(?P<filmaId>\d+)/$','filmak.views.bozkatzaileak'),

		url(r'^(?P<pk>\d+)/$',
	        DetailView.as_view(
	            model=Filma,
	            template_name='filmak/filmak_details.html')),
		url(r'^login/$','filmak.views.logeatu'),
		url(r'^logout/$','filmak.views.logout_bista'),
		#url(r'^signup/$',
	      # 'django.contrib.auth.views.login', {'template_name': 'signup/index.html'}),

		url(r'^signup/$', 'filmak.views.sortu_erabiltzailea'),


)