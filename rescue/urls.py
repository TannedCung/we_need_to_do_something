from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rescuer/', views.rescuer_list, name='rescuer_list'),
    path('rescuer/<int:rescuer_id>/', views.rescuer_detail, name='rescuer_detail'),
    path('rescuer/add/', views.add_rescuer, name='add_rescuer'),
    path('rescuer/<int:rescuer_id>/update/', views.update_rescuer, name='update_rescuer'),
    path('rescuer/<int:rescuer_id>/delete/', views.delete_rescuer, name='delete_rescuer'),
    path('victims/', views.victim_list, name='victim_list'),
    path('victims/<int:victim_id>/', views.victim_detail, name='victim_detail'),
    path('victims/add/', views.add_victim, name='add_victim'),
    path('victims/<int:victim_id>/update/', views.update_victim, name='update_victim'),
    path('victims/<int:victim_id>/delete/', views.delete_victim, name='delete_victim'),
    path('guest-help/', views.guest_help, name='guest_help'),
]
