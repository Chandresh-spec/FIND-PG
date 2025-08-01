
from django.urls import path
from . import views

urlpatterns = [
   
    
    path('pg_listing/',views.pg_listing,name="pg_listing"),
    path('pg_register/',views.pg_register,name="pg_register"),
    path('register_here/',views.register_here,name="register_here"),
    path('success_page/', views.success_view,name='success_page'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('premium_pg/',views.premium_pg,name='premium_pg'),
    path('pg/<int:pk>/',views.detailspage,name='detailspage'),
    path('search_pg/',views.search_pg,name='search_pg')



   
]
