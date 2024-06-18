from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.Signup,name="Signup"),
    path('login',views.Login,name="Login"),
    path('logout',views.Logout,name="Logout"),
    path('allemployees',views.Allemployees,name="Allemployees"),
    path('singleemployee',views.Singleemployee,name="Singleemployee"),
    path('addemployee',views.Addemployee,name="Addemployee"),
    path('deleteemployee/<int:empid>',views.deleteemployee,name="deleteemployee"),
    path('contact',views.Contact,name="contact"),
    path('updateemployee/<int:empid>',views.updateemployee,name="updateemployee"),
    path('about',views.about,name="about"),
    path('services',views.services,name="about"),
    path('doupdateemployee/<int:empid>',views.doupdateemployee,name="doupdateemployee"),
    
]