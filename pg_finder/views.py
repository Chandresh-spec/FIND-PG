from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import PG,RoomDetails
from .forms import PGform,UserRegistrationFrom
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def pg_listing(request):
    pg_list=PG.objects.all()
    rent_list=RoomDetails.objects.all()
    return render(request,'pg_listing.html',{'pg_list':pg_list,'rent_list':rent_list})


@login_required(login_url='login')
def pg_register(request):
    return render(request,'register_pg.html')

def success_view(request):
   return render(request,'success_page.html')


def register_here(request):
    if request.method== 'POST':
        form=PGform(request.POST,request.FILES)
        if form.is_valid():
             pg=form.save(commit=False)
             pg.user=request.user
             pg.save()
             return redirect('success_page')
        else:
            return render(request,'pg_registration.html',{'form':form})
    else:
        form=PGform()
        return render(request,'pg_registration.html',{'form':form})


def register_view(request):
    if request.method=='POST':
        form=UserRegistrationFrom(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        else:
            return  render(request,'register.html',{'form':form})
    else:
        form=UserRegistrationFrom()
        return render(request,'register.html',{'form':form})
    


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # messages.success(request, f"Welcome back, {username}!")
                return redirect("Homepage")
            # else:
                # messages.error(request, "Invalid username or password")
        # Even if invalid, re-render login with errors
        else:
        #    messages.error(request, "Invalid username or password")
           return render(request, 'login.html', {"form": form})

    else:
        # For GET request — show empty login form
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})

 
 
 
def logout_view(request):
    logout(request)
    # messages.success(request,"you have been logged out.")
    return redirect('login')




def premium(request,pk):
    pg=get_object_or_404(PG,pk=pk)
    items=PG.objects.all()
    return render(request,'premium.html',{'items':items,'pg':pg})



def detailspage(request,pk):
    pg=get_object_or_404(PG,pk=pk)
    rooms = RoomDetails.objects.filter(pg=pg).first()
    return render(request,'detailpage.html',{'pg':pg,'rooms':rooms})







 
 
 
 
 

 

 
 
 
 

 
 
 
 

 
 

















