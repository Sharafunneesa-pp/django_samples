from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def print_hello(request):
    movie_data={
       "movies": [{
        "title":"godfather",
        "year":2000,
        "summary":"old movie of mukesh",
        "success":False
    },{
        "title":"godfather",
        "year":2000,
        "summary":"old movie of mukesh",
        "success":False
    },{
        "title":"yodha",
        "year":2000,
       
        "success":False
    },{
        "title":"godfather",
        "year":2000,
        "summary":"old movie of mukesh",
        "success":False
    },{
        "title":"godfather",
        "year":2000,
        "summary":"old movie of mukesh",
        "success":False
    }]}
    return render(request,'page1.html',movie_data)
