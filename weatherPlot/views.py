import requests
import datetime
from datetime import datetime,timedelta,date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render
from django.template import Template,Context
from django.template.loader import get_template
from .forms import FilterForm,AddStation,AddTag
from .models import UserProfile,Station,DataPoint

@login_required
def landing_page_view(request):
	"""
	landing page view	
	"""
	if request.method == 'GET':	
		all_user_stations = UserProfile.objects.get(user=request.user).station_set.all()
		all_user_station_name = [x.station_name for x in all_user_stations]
		form = FilterForm()
		tag_form = AddTag()
		#print(request.user.)
		context = {
			'form':form,
			'tag_form':tag_form,
			'username':request.user.username,
			'all_user_station_name':all_user_station_name
		}
		return render(request,'weatherApp/landing_page.html',context)
		


def get_points_view(request):
	if request.method == 'POST' and request.is_ajax():
		"""
		This ajax request posts date range,parameter and returns temerature or humidity values of 
		pirticular dates.
		"""
		response_data = {}
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
				# print(temperature_list)
				# print(humidity_list)
				if temperature_list:
					response_data['temperature_list'] = temperature_list
					response_data['parameter'] = 'temperature'
				elif humidity_list:
					response_data['humidity_list'] = humidity_list	
					response_data['parameter'] = 'humidity'
					

				user_profile = UserProfile.objects.get(user=request.user)
				updated_list_obj = []
				for index,date in enumerate(date_list_obj):
					obj = DataPoint.objects.get_or_create(
									user_profile = user_profile,
									date = date,
									station_name = station_name
									)
					if temperature_list:
						obj[0].temperature_value = temperature_list[index]
						obj[0].save()
					

					elif humidity_list:
						obj[0].humidity_value = humidity_list[index]
						obj[0].save()		
					updated_list_obj.append(obj[0])
				
				print(updated_list_obj)	
				li_template = get_template('li_form.html')
				context = Context({'updated_list_obj':updated_list_obj,'parameter':parameter})
				li_template_data = li_template.render(context)
				#print(li_template_data)	
				response_data['error'] = False	
				response_data['date_list'] = date_list_obj
				response_data['li_template_data'] = li_template_data
				return JsonResponse(response_data)	
			except:
				response_data['error'] = True
				return JsonResponse(response_data)
		else:
			response_data['form_invalid'] = True 
			return JsonResponse(response_data)		

@login_required
def add_station_view(request):
	"""
		user can add stations which are not yet connected with his profile table
	"""
	if request.method == 'GET':
		form = AddStation()
		all_stations = Station.objects.all()
		all_user_stations = UserProfile.objects.get(user=request.user).station_set.all()
		all_user_station_name = [x.station_name for x in all_user_stations]
		new_station_list = []
		if len(all_user_station_name) > 0:	
			for station in all_stations:
				if station.station_name in all_user_station_name:
					pass
				else:
					new_station_list.append(station.station_name)
		else:
			new_station_list = [x.station_name for x in all_stations]				
		context = {
			'form':form,
			'all_stations':new_station_list
		}
		return render(request,'weatherApp/add_station_page.html',context)

	if request.method == 'POST':
		form = AddStation(request.POST)
		if form.is_valid():
			station_name = form.cleaned_data['station_name']
			profile_obj = UserProfile.objects.get(user=request.user)
			new_station_obj = Station.objects.get(station_name=station_name)
			new_station_obj.user_profile.add(profile_obj)
		return HttpResponseRedirect('/')


def add_tag_view(request):
	if request.method == 'POST' and request.is_ajax():
		response_data = {}
		form = AddTag(request.POST)
		data_id = request.POST.get('id')
		parameter = request.POST.get('parameter')
		print(data_id)
		if form.is_valid():
			tag_value = form.cleaned_data['tag_value']
			point_obj = DataPoint.objects.get(id=data_id)
			if parameter == 'temperature':
				point_obj.temperature_tag = tag_value
			else:
				point_obj.humidity_tag = tag_value
			point_obj.save()
			response_data['status'] = 'saved'		
			return JsonResponse(response_data)


