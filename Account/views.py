from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Accounts/home.html')


def login_page(request):
    return render(request,'Accounts/login.html')


def registration_page(request):
    return render(request,'Accounts/registration.html')    

def prof_page(request):
    return render(request,'Accounts/profile.html')    
