from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'machete/index.html')


def shop(request):


    return render(request, 'machete/shop.html')

def lodging(request):


    return render(request, 'machete/lodging.html')