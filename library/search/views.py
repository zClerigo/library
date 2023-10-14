from django.shortcuts import render, redirect
from django.http import HttpResponse
from .library_forms import LibraryForm
from django.contrib import messages
import datetime
import json
# from django.contrib import messages
# import json

booksList = [{"name" : "Harry Potter", "Author" : "JK Rowling"}, {"name" : "The Cat in the Hat", "Author" : "Dr. Suess"}, {"name" : "How the Grinch Stole Christmas", "Author" : "Dr. Suess"}, {"name" : "The Hunger Games","Author" : "Suzanne Collins"}, {"name" : "The Lord of the Rings", "Author" : "JRR Tolkien"}, {"name" : "To Kill a Mockingbird",  "Author" : "Harper Lee"}, {"name" : "Charlie and the Chocolate Factory", "Author" : "Roald Dahl"}]


def index(request):
   titlePage = "Search Index"
   return render(request, "search/index.html",context = {'titlePage' : titlePage,
                                                         'booksList' : booksList})
def input(request):
   if request.method == "POST":
        if "attribute" not in request.POST:
            messages.add_message(request, messages.ERROR, "The form sent is incomplete")
            return render(request, "search/input.html")        
        response = redirect("search:search_info")     
        response.set_cookie(key="search_data",value=json.dumps({"attribute": request.POST["attribute"],}), samesite ='Lax', max_age=datetime.timedelta(seconds=10))
        return response
   return render(request, "search/input.html")

def search_info(request):

    dico_cookies = request.COOKIES
    dico_context = {}
    if 'search_data' in dico_cookies:
        try:
            dico_search_data = json.loads(dico_cookies['search_data'])
            dico_context['key'] = dico_search_data
        except:
            messages.add_message(request, messages.ERROR, "There is an error on your search data")
    return render(request, "search/search_info.html", context={dico_context, booksList})

def list_view(request):
    dico_cookies = request.COOKIES
    dico_context = {}
    #name = ""
   # author = ""
    if 'search_data' in dico_cookies:
        try:
            data = json.loads(dico_cookies['search_data'])
            dico_context['name'] = data['name']
            dico_context['Author'] = data['author']
        except:
            messages.add_message(request, messages.ERROR, "There is an error on your search data")
    
    booksList.append(dico_context)
    return render(request, "search/list_view.html", context={'booksList': booksList})


def form1(request):
   if request.method == "POST":    
        response = redirect("search:list_view")     
        response.set_cookie(key="search_data",value=json.dumps({"name": request.POST["name"],"author": request.POST["author"],}), samesite ='Lax', max_age=datetime.timedelta(seconds=10))
        return response
   return render(request, "search/form1.html")

def form2(request):
   if request.method == "POST":
       form = LibraryForm(request.POST)
       if form.is_valid():
           # process the data
        response = redirect("search:list_view")
        response.set_cookie(key="search_data",value=json.dumps({"name": request.POST["name"],"author": request.POST["author"],}), samesite ='Lax', max_age=datetime.timedelta(seconds=10))
        return response
   else:
       form = LibraryForm()
   return render(request, "search/form2.html", {'library_form': form})

def delete_item(request):
    booksList.pop()
    return render(request, "search/list_view.html", context={'booksList': booksList})

def edit_item(request):
    booksList.pop()
    return render(request, "search/list_view.html", context={'booksList': booksList})
# def new_search_info(request):
    
#     dico_cookies = request.COOKIES
#     dico_context = {}
#     if 'game_data' in dico_cookies:
#         try:
#             dico_game_data = json.loads(dico_cookies['game_data'])
#             dico_context['game_data'] = dico_game_data
#         except:
#             messages.add_message(request, messages.ERROR, "There is an error on your game data")
#     return render(request, "games/new_search_info.html", context=dico_context)