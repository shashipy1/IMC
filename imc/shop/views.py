from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("ABOUT")

def contact(request):
    return HttpResponse("CONTACT")

def search(request):
    return HttpResponse("SEARCH")

def prodView(request):
    return HttpResponse("PRODUCT VIEWS")

def track(request):
    return HttpResponse("TRACKING")