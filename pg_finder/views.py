from django.shortcuts import render
from django.http import HttpResponse
from .models import PG,RoomDetails
# Create your views here.


def pg_listing(request):
    pg_list=PG.objects.all()
    rent_list=RoomDetails.objects.all()
    return render(request,'pg_listing.html',{'pg_list':pg_list,'rent_list':rent_list})