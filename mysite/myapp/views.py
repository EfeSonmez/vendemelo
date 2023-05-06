from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello world")


def products(request): 
    products = ["iphone","imac","ipad"]
    return HttpResponse("<h1>List of products</h1>")

