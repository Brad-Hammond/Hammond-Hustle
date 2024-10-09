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
    the user is added to the Employees group; otherwise, they are
    added to the Users group.
    '''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Get the code from the form
            code = form.cleaned_data.get('code')

            # Ensure the "Employees" group exists
            employees_group, created = Group.objects.get_or_create(name='Employees')
            users_group, created = Group.objects.get_or_create(name='Users')

            # Check the code and assign the user to the appropriate group
            if code == 'EMPLOYEE2024':
                user.groups.add(employees_group)
            else:
                user.groups.add(users_group)

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
    employees see only bookings for their assigned coach, and admins see all bookings.
    """
    is_user = request.user.groups.filter(name="Users").exists()
    is_employee = request.user.groups.filter(name="Employees").exists()
    is_admin = request.user.groups.filter(name="Admin").exists()

    # Retrieve bookings based on the user’s group
    if is_user:
        # Users see only their own bookings
        bookings = Booking.objects.filter(user=request.user)
    elif is_employee:
        # Employees see only bookings for users assigned to their coach
        if hasattr(request.user, 'coach'):
            bookings = Booking.objects.filter(coach=request.user.coach)
        else:
            bookings = []  # Employee has no coach assigned
    elif is_admin:
        # Admins see all bookings
        bookings = Booking.objects.all()
    else:
        bookings = []  # No bookings for others

    # Render the manage_bookings template with the bookings data
    return render(request, 'bookings/manage_bookings.html', {
        'bookings': bookings,
        'is_user': is_user,
        'is_employee': is_employee,
        'is_admin': is_admin
    })

# View for creating a booking
@login_required
def create_booking(request):
    """
    Allows users to create a new booking. Once submitted,
    the booking is saved with 'Pending' status. Displays a list
    of existing bookings and disables already booked times.
    """
    form = BookingForm(request.POST or None)

    # Handle form submission
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user  # Associate booking with logged-in user
        booking.status = 'Pending'
        booking.save()
        return redirect('manage_bookings')  # Redirect to manage bookings after saving

    # Retrieve existing bookings for the user
    existing_bookings = Booking.objects.filter(user=request.user)

    # Retrieve booked times across all bookings to disable in the form
    booked_times = Booking.objects.values_list('session_time', flat=True)
    booked_times_list = [dt.strftime("%Y-%m-%dT%H:%M") for dt in booked_times]

    # Render the form with existing bookings
    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'existing_bookings': existing_bookings,  # Pass existing bookings to template
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

@login_required
def delete_booking(request, booking_id):
    """
    Allows a user to delete their booking. Only the booking owner or an admin/employee can delete.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    # Only allow deletion if the booking belongs to the user or the user is an admin/employee.
    if booking.user == request.user or request.user.groups.filter(name__in=['Employees', 'Admin']).exists():
        booking.delete()
        return redirect('manage_bookings')
    else:
        # Redirect with a message if unauthorized
        return redirect('manage_bookings')