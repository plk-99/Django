from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s = '<h1> HELLO STUDENT WELCOME TO DJANGO</h1><br><h2>See you Later Student</h2><br><h3>Bye Student</h3>'
    return HttpResponse(s)