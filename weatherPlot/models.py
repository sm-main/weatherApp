from django.db import models
from django.conf import settings
# Create your models here.

class Stations(models.Model):
	station_name = models.CharField(max_length=40)
	


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	# stations = models.Foreignkey(Stations)