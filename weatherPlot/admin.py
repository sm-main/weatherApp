from django.contrib import admin
from .models import UserProfile,Station,DataPoint
# Register your models here.

admin.site.register(Station)
admin.site.register(UserProfile)
admin.site.register(DataPoint)
