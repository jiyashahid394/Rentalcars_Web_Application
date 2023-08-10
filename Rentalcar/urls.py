from django.contrib import admin
from django.urls import path
from Rentalcar import views
from .views import Booking, booking_confirmation

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("Silver", views.Silver, name='Silver'),
    path("Gold", views.Gold, name='Gold'),
    path("Platinum", views.Platinum, name='Platinum'),
    path("Booking", views.Booking, name='Booking'),
    path('booking_confirmation/', booking_confirmation, name='booking_confirmation'),


]