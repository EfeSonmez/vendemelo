from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    return HttpResponse("hello world")


def products(request): 
    products = Product.objects.all()
    context = { 
        'products':products
    }
    return render(request, 'myapp/index.html',context)

def product_detail(request,id):
    product = Product.objects.get(id=id)               ## Product id
    context={
        'product':product
    }
    return render(request, 'myapp/detail.html',context)                 # return HttpResponse('The product id is '+ str(id)) ctrl k c

