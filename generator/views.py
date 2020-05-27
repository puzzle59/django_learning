from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters=list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get('uppercase'):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVXYZ"))
    if request.GET.get("specials"):
        characters.extend(list("@€*(-#~<>})"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    lenght=int(request.GET.get('lenght','9'))
    your_password=""

    for i in range(lenght):
        your_password+=random.choice(characters)
    return render(request,"generator/password.html",{'password':your_password})

def about(request):
    return render(request,'generator/about_page.html')
