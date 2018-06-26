from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'
urlpatterns = [
	path(r'login/', auth_views.login, name = 'login'),
	path(r'logout/', auth_views.logout, {'next_page':'/'}, name = 'logout'),
	path(r'signup/', views.signup, name = 'signup'), 
	


]
