"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from machete import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('lodging', views.lodging, name='lodging'),
    path('lessons', views.lessons, name='lessons'),
    path('rentals', views.rentals, name='rentals'),
    path('club', views.club, name='club'),
    path('facilities', views.facilities, name='facilities'),
    path('trips', views.trips, name='trips'),
    path('spot', views.spot, name='spot'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('contact', views.contact, name='contact'),
    path('track-click/<str:link_name>/', views.track_click_ajax, name='track_click_ajax'),
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)