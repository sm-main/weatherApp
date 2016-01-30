from django import forms
from .models import UserProfile,Station

PARAMETER_CHOICES = (('Temperature','Temperature'),('Humidity','Humidity'))

class FilterForm(forms.Form):
	station_name = forms.CharField(
							widget=forms.TextInput(
								attrs={
									'class':'form-control'
							}))

	parameter = forms.ChoiceField(
								choices=PARAMETER_CHOICES,
								widget=forms.Select(
									attrs={
										'class':'form-control'
								}))

	date_start=forms.CharField(
							widget=forms.TextInput(
								attrs={
									'class':'date start form-control',
									'required':'true'
								}))
	date_stop=forms.CharField(
							widget=forms.TextInput(attrs={
								'class':'date end form-control',	
								}))

class AddStation(forms.Form):
	station_name = forms.CharField(
							widget=forms.TextInput(
								attrs={
									'class':'form-control'
								}))	

class AddTag(forms.Form):
	tag_value = forms.CharField(
							widget=forms.TextInput())	