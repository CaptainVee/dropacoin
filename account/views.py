from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile
from django.contrib import messages, auth
from .forms import UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
# Create your views here.


def welcome(request):
	'''this function is to redirect from login page to workspace list passing the username 
	of the logged in user as a parameter'''
	username = request.user.username
	if username == '':
		return render(request, 'account/landingPage.html', {'title': 'dropacoin'})
	# else:
	# 	return redirect('dashboard', username)


def register(request):
	if request.method == 'POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		if password1 == password2:
			if (User.objects.filter(username=username).exists()):
				messages.warning(request,'User Name Already Exists')
				return redirect('signup')
			elif (User.objects.filter(email=email).exists()):
				messages.warning(request,'Email Already Exists')
				return redirect('signup')
			else:
				user=User.objects.create_user(
					password=password1,  
					username=username, 
					first_name=first_name, 
					last_name=last_name, 
					email=email,
					)
				user.save()
				user=auth.authenticate(username=username,password=password)
				auth.login(request,user)
				messages.success(request,'User Created')
				return redirect('landing_page')
		else:
			messages.warning(request,'User Password MisMatching')
			return render(request, 'account/signup.html')
	else:
		return render(request, 'account/signup.html') 

def login(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	if request.method == 'POST':
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('landing_page')

		else:
			messages.warning(request,'Invalid Credentials')
			return redirect('login')
	else:
		return render(request,'account/login.html')


@login_required
def profile(request):
	if request.method == 'POST':
		userForm = UserUpdateForm(request.POST, instance=request.user)
		profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if profileForm.is_valid():
			userForm.save()
			profileForm.save()
			messages.success(request, f'Your Account has been updated!')
			return redirect('profile')

	else:
		userForm = UserUpdateForm(instance=request.user)
		profileForm = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'userForm': userForm,
		'profileForm': profileForm,
	}

	return render(request, 'account/profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('landing_page')