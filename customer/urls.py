from django.urls import path
from django.conf.urls import include, url
from . import views
from . import views, restviews
from rest_framework import routers

#rest web services
router = routers.DefaultRouter()
router.register(r'emps', restviews.EmpViewSet)# mapping the url with view sets

urlpatterns = [

    path('create/', views.handleCreate1, name="index page"),
    path('student/', views.handleStudent1, name="student page"),
    path('', views.handleLogin, name="login-page"),
    path('loginEmployee/', views.handleLogin, name="loginEmployee-page"),
    path('logoutEmployee/', views.handleEmpLogout, name="logout-Employee"),
    path('getall/', views.handleGetall, name="getall-page"),
    path('getemp/', views.handleGet, name="getEmp-page"),
    path('getemp1/', views.handleGet1, name="getemp1 page"),
    path('dltemp/', views.handleDlt, name="delete-page"),
    path('editEmployee/', views.handleUpdate, name="index page"),
    path('updateEmployee/', views.handleUpdate1, name="updateEmployee page"),
    path('sortemp/', views.handlSortEmp, name="sortEmployee page"),
    path('onetoone/', views.handleOnetoone, name="onetoone-page"),
    path('manytoone/', views.handleManytoone, name="manytoone-page"),
    path('manytomany/', views.handleManytomany, name="manytomany-page"),
    path('rest/', include(router.urls)),
    path('rest1/getuser', restviews.get_users),
    path('rest1/adduser', restviews.add_user),
]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

