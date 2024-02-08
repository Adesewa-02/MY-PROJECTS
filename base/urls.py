from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('registrationpage/',views.registrationpage),
    path('loginpage/',views.loginpage),
    path('bookspage/',views.bookspage),
    path('authorspage/',views.authorspage),
    path('aboutuspage/',views.aboutuspage),
    path('customersprofile/str:info>',views.customersprofile,name="customersprofile")
]
