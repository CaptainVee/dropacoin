from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome, dashboard, get_amount, verify_funds,ExploreView


urlpatterns = [
	path('', welcome, name='landing_page'),
	path('profile/explore/', ExploreView.as_view(), name='explore'),
	path('get_amount/<str:username>/', get_amount, name='get-amount'),
	path('verify_funds/', verify_funds, name='verify-funds'),
	path('<str:username>/', dashboard, name='dashboard'),

]
