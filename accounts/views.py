from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from .forms import LoginForm,RegistrationForm



def logout_view(request):
	print ('logging out')
	logout(request)
	return HttpResponseRedirect('%s'%(reverse("auth_login")))

def login_view(request):
	if request.method == 'GET':
		form = LoginForm()
		context = {
			'form':form
		}
		return render(request, "form.html", context)
	else:		
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			login(request, user)
			#messages.success(request, "Successfully Logged In. Welcome Back!")
			return HttpResponseRedirect("/")
		else:
			context = {
				'errors':form.errors
			}
			return render(request,'form.html',context)
		


def registration_view(request):
	form = RegistrationForm(request.POST or None)
	btn = "Register"
	if form.is_valid():
		new_user = form.save(commit=False)
		new_user.save()
		return HttpResponseRedirect("/")

	context = {
		 "form": form,
		 "submit_btn": btn,
	}
	return render(request, "form.html", context)