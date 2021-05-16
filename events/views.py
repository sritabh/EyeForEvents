from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("This is event manager app, anything related to event will happen in this like creating new event,viewing event etc.")