from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def firstapp(request):
    return render(request,'firstapp/dj_index.html')