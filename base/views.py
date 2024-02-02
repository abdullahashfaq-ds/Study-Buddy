from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')


def room(request):
    return HttpResponse('Room')
