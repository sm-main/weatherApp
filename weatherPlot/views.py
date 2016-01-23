import requests
import datetime
from datetime import datetime,timedelta,date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render
from .forms import FilterForm
from .models import UserProfile,Station

@login_required
def landing_page_view(request):
	"""

	"""
	if request.method == 'GET':	
		form = FilterForm()
		#print(request.user.)
		context = {
			'form':form,
			'username':request.user.username
		}
		return render(request,'weatherApp/landing_page.html',context)
		


def get_points_view(request):
	if request.method == 'POST' and request.is_ajax():
		"""

		"""
		response_data = {}
		all_user_stations = UserProfile.objects.get(user=request.user).stations
		form = FilterForm(request.POST)
		if form.is_valid():
			station_name = form.cleaned_data['station_name']
			parameter = form.cleaned_data['parameter']
			date_start = form.cleaned_data['date_start']
			date_stop = form.cleaned_data['date_stop']

			date_start_obj = datetime.strptime(date_start,'%Y-%m-%d').date()
			date_stop_obj = datetime.strptime(date_stop,'%Y-%m-%d').date()

			date_differerce = date_stop_obj - date_start_obj
			date_list_str = []
			date_list_obj = []
			for i in range(date_differerce.days +1):
				temp = date_start_obj + timedelta(i)
				date_list_obj.append(str(temp))
				temp_str = str(temp).replace('-','')
				date_list_str.append(temp_str)

			temperature_list = []
			humidity_list = []	
			try:
				for datex in date_list_str:
					api_url = 'http://api.wunderground.com/api/210963837bbe7173//history_'+datex+'/q/India/'+station_name+'.json'
					data = requests.get(api_url).json()
					if parameter == 'Humidity':
						humidity = data['history']['dailysummary'][0]['humidity']
						humidity_list.append(humidity)
					if parameter == 'Temperature':
						temperature = data['history']['dailysummary'][0]['meantempm']
						temperature_list.append(temperature)
				print(temperature_list)
				print(humidity_list)
				if temperature_list:
					response_data['temperature_list'] = temperature_list
					response_data['parameter'] = 'temperature'
				elif humidity_list:
					response_data['humidity_list'] = humidity_list	
					response_data['parameter'] = 'humidity'
				response_data['error'] = False	
				#print(date_list_obj,'list_obje')
				response_data['date_list'] = date_list_obj			
				return JsonResponse(response_data)	
			except:
				response_data['error'] = True
				return JsonResponse(response_data)

@login_required
def add_station_view(request):
	pass
