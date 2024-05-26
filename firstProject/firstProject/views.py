from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. you are at chai our Django Home page")
    return render(request,'websites/index.html')

def about(request):
    return HttpResponse("Hello, world. you are at chai our Django about page")

def contact(request):
    return HttpResponse("Hello, world. you are at chai our Django contact page")












