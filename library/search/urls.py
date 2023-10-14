from django.urls import path

from . import views

app_name = "games"

urlpatterns = [
   path("", views.index, name="index"),
   path('input/', views.input, name='input'),
#    path('forms/', views.forms, name='forms'),
   path('search_info/', views.search_info, name='search_info'),
    path('list_view/', views.list_view, name='list_view'),
    path('form1/', views.form1, name='form1'),
   path('form2/', views.form2, name='form2'),
   path('delete_item/', views.delete_item, name='delete_item'),
   path('edit_item/', views.edit_item, name='edit_item'),
 #   path('update/<int:entry_id>/', views.update_data, name='update_data'),

#    path('new_forms/', views.new_forms, name='new_forms'),
#    path('new_game_info/', views.new_game_info, name='new_game_info'),

]