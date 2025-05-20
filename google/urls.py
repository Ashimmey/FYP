"""
URL configuration for google project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth import views as auth_views
from mainApp import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('insertuser',views.insertuser,name='insertuser'),
    path('google/callback/', views.google_login_callback, name='google_login_callback'),
    path('starter/', views.starter_view, name='starter'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    path('',views.home,name='home'),
    path('logout_user',views.logout_user,name='logout'),
    path('item/',views.item,name='item'),
    path('addPitch/',views.addpitch,name='addPitch'),
    path('addpost/',views.addpost,name='addpost'),
    path('userdashboard/',views.userdash,name='userdash'),
    path('admindashboard.html', views.admin_dashboard, name='admin_dashboard'),
    path('opportunities/<int:pk>/', views.opportunity_detail, name='opportunity_detail'),
     path('opportunity/edit/<int:id>/', views.opportunity_edit, name='opportunity_edit'),
    path('opportunity/delete/<int:id>/', views.opportunity_delete, name='opportunity_delete'),
    path('chat/<str:room_name>/',views.chat_room,name='chat'),
]

