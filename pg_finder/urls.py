
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('',views.pg_listing,name="pg_listing"),
    path('pg_register/',views.pg_register,name="pg_register"),
    path('register_here/',views.register_here,name="register_here"),
    path('success/', views.success_page,name='success_page'),
    path('register/',views.register,name='register')

   
]
