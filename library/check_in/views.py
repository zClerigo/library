from django.shortcuts import render, redirect
from django.http import HttpResponse
from .books_forms import BookForm
from django.contrib import messages
import datetime
import json

def index(request):
   # print("This is the books index...")
   titlePage = "Check In:"
   booksList = [{"name" : "Harry Potter", "Series" : True}, {"name" : "The Cat in the Hat", "Series" : True}, {"name" : "How the Grinch Stole Christmas", "Series" : False}, {"name" : "The Hunger Games", "Series" : True}, {"name" : "The Lord of the Rings", "Series" : True}, {"name" : "To Kill a Mockingbird", "Series" : False}, {"name" : "Charlie and the Chocolate Factory", "Series" : False}]
   return render(request, "check_in/index.html", context = {'titlePage' : titlePage,
                                                         'booksList' : booksList})
   
# def cookies(request):
#    response = render(request, "games/cookies.html")
#    response.set_cookie(key ="HI", value = "Bonjour")
#    return response

def cookies(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "library/cookies.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr,
max_age=datetime.timedelta(seconds=10))
   #  expires=datetime.datetime(2023, 10, 2, 18, 23))
   return response

def new_forms(request):
   if request.method == "POST":
       form = BookForm(request.POST)
       if form.is_valid():
           # process the data
        response = redirect("library:new_book_info")
        response.set_cookie(key="book_data", value=json.dumps(
{'id_name': request.POST['name'],
'id_characters': request.POST['characters'],
'id_genre': request.POST['genre']}))
        return response
   else:
       form = GameForm()
   return render(request, "library/new_forms.html", {'book_form': form})
