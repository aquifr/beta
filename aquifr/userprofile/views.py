from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user and request.user.is_authenticated:
        return HttpResponse("Welcome, {}!".format(request.user) )
    return HttpResponse("This is the profile page. You are not currently logged in.")
