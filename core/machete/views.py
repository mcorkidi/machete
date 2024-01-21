from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'machete/index.html')


def shop(request):


    return render(request, 'machete/shop.html')

def lodging(request):

    return render(request, 'machete/lodging.html')

def lessons(request):

    return render(request, 'machete/lessons.html')

def rentals(request):

    return render(request, 'machete/rentals.html')

def club(request):

    return render(request, 'machete/club.html')

def facilities(request):

    return render(request, 'machete/facilities.html')

def trips(request):

    return render(request, 'machete/trips.html')