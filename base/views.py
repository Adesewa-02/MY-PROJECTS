from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

customers = [
    {'id': 1, 'name': 'Adesewa', 'interest': 'Finance'},
    {'id': 2, 'name': 'Esther', 'interest': 'Relationship'},
    {'id': 3, 'name': 'Peter', 'interest': 'Love'},
    {'id': 4, 'name': 'James', 'interest': 'Marriage'},
    {'id': 5, 'name': 'Miracle', 'interest': 'Spiritual Growth'},
    {'id': 6, 'name': 'Paul', 'interest': 'Prayer'}
]

customers_profile = {'details': customers}

def homepage(request): 
    return render(request, 'home.html', customers_profile)

def registrationpage(request):
    return render(request, 'register.html')

def loginpage(request):
    return render(request, 'login.html')

def bookspage(request):
    return render(request, 'books.html')

def authorspage(request):
    return render(request, 'authors.html')

def aboutuspage(request):
    return render(request, 'aboutus.html')

def customersprofile(request, info,):
    det = None
    for d in details:
        if d['id'] == int(info):
            det = d
    return render(request,'customer.html',{'details':customers})