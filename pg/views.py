from django.shortcuts import render
from django.http import HttpResponse



def hii(request):
    return HttpResponse("hiii this is chandresh moger")

def helo(request):
    return render(request,'index.html')