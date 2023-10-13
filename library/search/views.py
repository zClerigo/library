from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
   titlePage = "Search Index"
   booksList = [{"name" : "Harry Potter", "Series" : True, "Author" : "JK Rowling"}, {"name" : "The Cat in the Hat", "Series" : True, "Author" : "Dr. Suess"}, {"name" : "How the Grinch Stole Christmas", "Series" : False, "Author" : "Dr. Suess"}, {"name" : "The Hunger Games", "Series" : True, "Author" : "Suzanne Collins"}, {"name" : "The Lord of the Rings", "Series" : True, "Author" : "JRR Tolkien"}, {"name" : "To Kill a Mockingbird", "Series" : False, "Author" : "Harper Lee"}, {"name" : "Charlie and the Chocolate Factory", "Series" : False, "Author" : "Roald Dahl"}]
   return render(request, "search/index.html",context = {'titlePage' : titlePage,
                                                         'booksList' : booksList})
def input(request):
   dico_cookies = request.COOKIES
   visit_nbr = 0
   if 'visit_nbr' in dico_cookies:
       try:
           visit_nbr = int(dico_cookies['visit_nbr']) + 1
       except:
           visit_nbr = 1
   else:
       visit_nbr = 1
   response = render(request, "search/input.html",
                     context={'visit_nbr': visit_nbr})
   response.set_cookie(key="visit_nbr", value=visit_nbr,
max_age=datetime.timedelta(seconds=10))
   #  expires=datetime.datetime(2023, 10, 2, 18, 23))
   return response