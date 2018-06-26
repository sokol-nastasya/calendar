from django.urls import path
from mainApp import views

app_name = 'mainApp'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('calendar', views.calendar, name = 'calendar'),
	path('entry/<int:pk>', views.details, name = 'details' ),
	path('entry/add', views.add, name = 'add'),
	path('entry/delete/<int:pk>', views.delete, name = 'delete'),

]
