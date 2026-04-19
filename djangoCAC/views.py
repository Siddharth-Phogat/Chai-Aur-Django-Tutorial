from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Siddharth. You are at Home Page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello Siddharth. You are at About Page.")

def contact(request):
    return HttpResponse("Hello Siddharth. You are at Contact Page.")