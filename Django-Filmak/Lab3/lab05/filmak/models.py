from django.db import models
from django.contrib.auth.models import User,UserManager

class Filma(models.Model):

	izenburua=models.CharField(max_length=100)
	zuzendaria=models.CharField(max_length=60)
	urtea=models.IntegerField(max_length=11)
	generoa=models.CharField(max_length=2)
	sinopsia=models.CharField(max_length=500)
	bozkak=models.IntegerField(max_length=11)
	class Meta:
		verbose_name_plural="filmak"
	
	def __unicode__(self):
		return self.izenburua +'-' +self.zuzendaria +'-'+ unicode(self.urtea) +'-'+ self.generoa+ '-' +self.sinopsia +'-' +unicode(self.bozkak) 


class Bozkatzailea(models.Model):
	erabiltzailea=models.OneToOneField(User)
	gogoko_filmak=models.ManyToManyField(Filma)
	class Meta:
		verbose_name_plural="bozkatzaileak"
	def __unicode__(self):
		return unicode(self.erabiltzailea.username)








	
# Create your models here.



