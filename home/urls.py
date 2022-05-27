
from django import views
from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index,name='index'),
    path("meabout",views.meabout,name='meabout'),
    path("projects",views.projects,name='projects'),
    path("contact",views.contact,name='contact'),
    path("skill",views.skill,name='skill'),
    path("certificates",views.certificates,name='certificates'),
    path("social",views.social,name='social'),
    
]
