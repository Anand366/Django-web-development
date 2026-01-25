from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("Hello i am about page")

def contact(request):
    return HttpResponse(
        "Hello i am <b>Contact page</b><br>"
        "Mobile No. 564496541985<br>"
        "Email :- anandrajashwin356@gmail.com<br>"
        "Address :- chandi chowk, Pune, India"
    )

def Home(request):
    return render(request, 'index.html')
def djang(request):
    return render(request,'ghar.html')