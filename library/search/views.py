from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

# from .games_forms import GameForm
# from django.contrib import messages
# import json

def index(request):
   titlePage = "Search Index"
   booksList = [{"name" : "Harry Potter", "Series" : True, "Author" : "JK Rowling"}, {"name" : "The Cat in the Hat", "Series" : True, "Author" : "Dr. Suess"}, {"name" : "How the Grinch Stole Christmas", "Series" : False, "Author" : "Dr. Suess"}, {"name" : "The Hunger Games", "Series" : True, "Author" : "Suzanne Collins"}, {"name" : "The Lord of the Rings", "Series" : True, "Author" : "JRR Tolkien"}, {"name" : "To Kill a Mockingbird", "Series" : False, "Author" : "Harper Lee"}, {"name" : "Charlie and the Chocolate Factory", "Series" : False, "Author" : "Roald Dahl"}]
   return render(request, "search/index.html",context = {'titlePage' : titlePage,
                                                         'booksList' : booksList})
def input(request):
   if request.method == "POST":
        if "author" not in request.POST:
            messages.add_message(request, messages.ERROR, "The form sent is incomplete")
            return render(request, "search/input.html")        
        response = redirect("search:search_info")     
        response.set_cookie(key="search_data",value=json.dumps({"author": request.POST["author"],}))
        return response
   return render(request, "search/input.html")