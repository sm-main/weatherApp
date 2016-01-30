from django.db import models
from django.conf import settings
# Create your models here.



class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.user.username

class Station(models.Model):
	station_name = models.CharField(max_length=40)
	user_profile = models.ManyToManyField(UserProfile,blank=True)
	def __str__(self):
		return self.station_name


class DataPoint(models.Model):
	user_profile = models.ForeignKey(UserProfile)
	station_name = models.CharField(max_length=40)
	date = models.DateField()
	temperature_value = models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)
	temperature_tag = models.CharField(max_length=500,blank=True)
	humidity_value = models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)
	humidity_tag = models.CharField(max_length=500,blank=True)

	def __str__(self):
		return self.user_profile.user.username +self.station_name
