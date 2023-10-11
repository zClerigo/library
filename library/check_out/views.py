from django.shortcuts import render, redirect
from django.http import HttpResponse
from .games_forms import GameForm
from django.contrib import messages
import datetime
import json

def index(request):
   print("This is the library index...")
   titlePage = "Library Index"
   libraryList = [{"name" : "Elder Scrolls: Oblivion", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Furry Shades of Gray", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Grand Theft Auto 6", "Franchise" : False, "ethicallyAmbiguous" : True}, {"name" : "Elden Ring", "Franchise" : True, "ethicallyAmbiguous" : False}, {"name" : "Minecraft", "Franchise" : True,  "ethicallyAmbiguous" : False}]
   return render(request, "games/index.html", context = {'titlePage' : titlePage,
                                                         'libaryList' : libraryList})
   
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

def forms(request):
    if request.method == "POST":
        if "fav_genre" not in request.POST or "fav_game" not in request.POST:
            messages.add_message(request, messages.ERROR, "The form sent is incomplete")
            return render(request, "library/forms.html")        
        response = redirect("library:game_info")     
        response.set_cookie(key="game_data",value=json.dumps({"fav_game": request.POST["fav_game"],
             "fav_genre": request.POST["fav_genre"],}))
        return response
    return render(request, "library/forms.html")

def game_info(request):
    
    dico_cookies = request.COOKIES
    dico_context = {}
   # import pdb;pdb.set_trace()
    if 'game_data' in dico_cookies:
        try:
            dico_game_data = json.loads(dico_cookies['game_data'])
            dico_context['game_data'] = dico_game_data
         #   import pdb;pdb.set_trace()
        except:
            messages.add_message(request, messages.ERROR, "There is an error on your library data")
    #import pdb;pdb.set_trace()
    return render(request, "library/game_info.html", context=dico_context)

def new_forms(request):
   if request.method == "POST":
       form = GameForm(request.POST)
       if form.is_valid():
           # process the data
        response = redirect("library:new_game_info")
        response.set_cookie(key="game_data", value=json.dumps(
{'id_name': request.POST['name'],
'id_characters': request.POST['characters'],
'id_genre': request.POST['genre']}))
        return response
   else:
       form = GameForm()
   return render(request, "games/new_forms.html", {'game_form': form})


def new_game_info(request):
    
    dico_cookies = request.COOKIES
    dico_context = {}
    if 'game_data' in dico_cookies:
        try:
            dico_game_data = json.loads(dico_cookies['game_data'])
            dico_context['game_data'] = dico_game_data
        except:
            messages.add_message(request, messages.ERROR, "There is an error on your game data")
    return render(request, "games/new_game_info.html", context=dico_context)