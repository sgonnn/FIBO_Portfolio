from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'activities/index.html')

def createActivity(request):
    return render(request, 'activities/createActivity.html')
