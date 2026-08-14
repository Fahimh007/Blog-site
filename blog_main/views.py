
from django.shortcuts import render
# from django.http import HttpResponse
# from ../templates import *

def home(request):
    # return HttpResponse("<h1>Hello, welcome to my blog!</h1>")
    return render(request, 'home.html')