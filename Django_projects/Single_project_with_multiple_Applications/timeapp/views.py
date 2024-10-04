from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo_view(request):
    time = datetime.datetime.now()
   
    return HttpResponse( '<h1>Hello Current time and Date is :'+str(time)+'</h1>')