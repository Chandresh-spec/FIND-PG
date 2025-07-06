
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('',views.pg_listing,name="pg_listing")
   
]
