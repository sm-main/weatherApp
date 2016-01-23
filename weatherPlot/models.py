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


