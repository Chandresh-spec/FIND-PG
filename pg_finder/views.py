from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PG,RoomDetails
from .forms import PGform,UserRegistrationFrom
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.


def pg_listing(request):
    pg_list=PG.objects.all()
    rent_list=RoomDetails.objects.all()
    return render(request,'pg_listing.html',{'pg_list':pg_list,'rent_list':rent_list})


@login_required
def pg_register(request):
    return render(request,'register_pg.html')

def success_page(request):
   return redirect('success_page')


def register_here(request):
    if request == 'POST':
        form=PGform(request.POST)
        if form.is_valid():
             pg=form.save(commit=False)
             pg.user=request.user
             pg.save()
             return redirect('success_page')
    else:
        form=PGform()
    
    return render(request,'pg_registration.html',{'form':form})


def register(request):
    if request=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('Homepage')
        else:
            return  render(request,'register.html',{'form':form})
    else:
        form=UserRegistrationFrom()
        return render(request,'register.html',{'form':form})








