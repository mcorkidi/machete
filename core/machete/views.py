from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    if request.method == 'POST' and 'email_submit' in request.POST:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        
        if email:  # Basic check to avoid blank email
            # Save the contact
            Contact.objects.create(name=name, email=email)
            messages.success(request, "Thank you for subscribing!")
            return redirect('index')  # Redirect to prevent form resubmission on page refresh
        else:
            messages.error(request, "Please enter a valid email.")
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

def spot(request):

    return render(request, 'machete/spot.html')

def restaurant(request):

    return render(request, 'machete/restaurant.html')

def contact(request):

    return render(request, 'machete/contact.html')