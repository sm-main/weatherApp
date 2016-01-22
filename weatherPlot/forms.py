from django import forms


PARAMETER_CHOICES = (('Temperature','Temperature'),('Humidity','Humidity'))

class FilterForm(forms.Form):
	station_name = forms.CharField(
							max_length=40,
							widget=forms.TextInput(
								attrs={
									'class':'form-control typeahead',
									'required':'true'
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