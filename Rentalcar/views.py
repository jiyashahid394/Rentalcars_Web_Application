from django.shortcuts import render,HttpResponse,redirect
from Rentalcar.models import Contact
from Rentalcar.models import booking
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c1 = Contact(name=name, email=email, subject=subject, message=message)
        c1.save()
    return render(request, 'contact.html')

def Silver(request):
    return render (request, 'Silver.html')

def Gold(request):
    return render (request, 'Gold.html')

def Platinum(request):
    return render (request, 'Platinum.html')

def about(request):
    return render (request, 'about.html')

def booking_confirmation(request):
    return render (request, 'booking_confirmation.html')

def Booking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        fdate = request.POST.get('fdate')
        tdate = request.POST.get('tdate')
        car = request.POST.get('car')  # Get the selected car option
        
        booking_instance = booking(name=name, email=email, number=number, fdate=fdate, tdate=tdate, car=car)
        booking_instance.save()
        
       
        return redirect('booking_confirmation')  # Redirect to a booking confirmation page
    
    return render(request, 'Booking.html')



