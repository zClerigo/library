from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
   path("", views.index, name="index"),
#    path('cookies/', views.cookies, name='cookies'),
#    path('forms/', views.forms, name='forms'),
#    path('game_info/', views.game_info, name='game_info'),
#    path('new_forms/', views.new_forms, name='new_forms'),
#    path('new_game_info/', views.new_game_info, name='new_game_info'),

]