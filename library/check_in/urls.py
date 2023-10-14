from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
   path("", views.index, name="index"),
   path('cookies/', views.cookies, name='cookies'),
   path('new_forms/', views.new_forms, name='new_forms'),


]