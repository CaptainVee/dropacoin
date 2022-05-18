from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, login, profile, logout_view


urlpatterns = [
	path('signup/', register, name='signup'),
	path('login/', login, name='login'),
	path('user/profile/', profile, name='profile'),
	path('logout/', logout_view, name='logout'),
]
