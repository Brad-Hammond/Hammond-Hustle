from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.http import JsonResponse  # Import for JSON response if needed
from django.utils.dateparse import parse_datetime  # Import if working with date parsing
import json  # Import json module to handle JSON data
from .models import Booking
from .forms import BookingForm, FeedbackForm, CustomUserCreationForm

# Create your views here.

@login_required
def booking_page(request):
    return render(request, 'booking.html')

# View to render base.html for the home/root URL
def home(request):
    # Check if the user is authenticated and belongs to the "Users" group
    is_user = False
    if request.user.is_authenticated and request.user.groups.filter(name='Users').exists():
        is_user = True
    
    return render(request, 'base.html', {'is_user': is_user})

# View for user signup
def signup(request):
    '''
    Handles user signup. If a special employee code is provided,
    the user is added to the Employee group; otherwise, they are
    added to the User group.
    '''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get the code from the form
            code = form.cleaned_data.get('code')

            # Check the code and assign the user to the appropriate group
            if code == 'EMPLOYEE2024':
                employee_group = Group.objects.get(name='Employee')
                user.groups.add(employee_group)
            else:
                user_group = Group.objects.get(name='User')
                user.groups.add(user_group)

            # Log the user in and redirect them
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

@login_required
def manage_bookings(request):
    """
    Displays a list of bookings. Users see only their bookings,
    while employees and admins see all bookings.
    """
    if request.user.groups.filter(name='Users').exists():
        bookings = Booking.objects.filter(user=request.user)
    elif request.user.groups.filter(name='Employees').exists() or request.user.groups.filter(name='Admin').exists():
        bookings = Booking.objects.all()
    return render(request, 'bookings/manage_bookings.html', {'bookings': bookings})

# View for creating a booking
@login_required
def create_booking(request):
    """
    Allows users to create a new booking. Once submitted,
    the booking is saved with 'Pending' status.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = 'Pending'
            booking.save()
            return redirect('manage_bookings') 
    else:
        form = BookingForm()


 # Retrieve booked times for the selected coach
    booked_times = Booking.objects.values_list('session_time', flat=True)
    booked_times_list = [dt.strftime("%Y-%m-%dT%H:%M") for dt in booked_times]


    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'booked_times_json': json.dumps(booked_times_list)  # Pass booked times as JSON to the template
    })

@login_required
def booking_confirmation(request, booking_id):
    """
    Displays a confirmation page after a booking is created.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

# View for employees/admins to accept a booking
@login_required
@permission_required('bookings.can_accept_booking', raise_exception=True)
def accept_booking(request, booking_id):
    """
    Allows employees or admins to accept a booking, changing its status to 'Accepted'.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Accepted'
    booking.save()
    return redirect('manage_bookings')

# View for employees to leave feedback for an accepted booking
@login_required
@permission_required('bookings.can_accept_booking', raise_exception=True)
def leave_feedback(request, booking_id):
    """
    Allows employees to leave feedback for a booking if it has been accepted.
    """
    booking = get_object_or_404(Booking, id=booking_id) 
    if booking.status != 'Accepted':
        return redirect('manage_bookings')

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=booking)
        if form.is_valid():
            form.save() 
            return redirect('manage_bookings')
    else:
        form = FeedbackForm(instance=booking)

    return render(request, 'bookings/leave_feedback.html', {'form': form, 'booking': booking})

# View for users to view feedback on their booking
@login_required
def view_feedback(request, booking_id):
    """
    Allows users to view feedback left by an employee on their booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != request.user:
        return redirect('manage_bookings')

    return render(request, 'bookings/view_feedback.html', {'booking': booking})