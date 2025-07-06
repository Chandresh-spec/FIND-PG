
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('',views.pg_listing,name="pg_listing"),
    path('pg_register/',views.pg_register,name="pg_register"),
   
]
