from django.shortcuts import render, redirect
from .models import Contact, ClickWhatsApp
from django.contrib import messages
from django.http import JsonResponse

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

def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    for attr in data.keys():
        #will print the data line by line
        print(attr,' '*13+'\t->\t',data[attr])
    return data
def track_click_ajax(request, link_name):
    if request.method == "POST":
        print('true')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        ipCall = ipInfo(ip)
        try: 
            if ipCall['bogon'] ==True:
                country = 'NA'
            else: 
                country = ipCall['country']
        except: 
            country = ipCall['country']
        newClick = ClickWhatsApp(country=country, from_site=link_name)
        newClick.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

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