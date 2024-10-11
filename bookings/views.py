from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Streamlined imports
from django.contrib.auth.models import Group
from .models import Booking, Profile
from .forms import BookingForm, CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
import json

# Render base.html for the home/root URL
def home(request):
    is_user = request.user.is_authenticated and request.user.groups.filter(name='Users').exists()
    return render(request, 'base.html', {'is_user': is_user})

# User signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            code = form.cleaned_data.get('code')
            employees_group, _ = Group.objects.get_or_create(name='Employees')
            users_group, _ = Group.objects.get_or_create(name='Users')
            if code == 'EMPLOYEE2024':
                user.groups.add(employees_group)
            else:
                user.groups.add(users_group)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Manage bookings view
@login_required
def manage_bookings(request):
    # Check for user roles
    is_user = request.user.groups.filter(name="Users").exists()
    is_employee = request.user.groups.filter(name="Employees").exists()
    is_admin = request.user.groups.filter(name="Admin").exists()

    # Admin view: if the user is a superuser, staff, or in the Admin group, show all bookings
    if request.user.is_superuser or request.user.is_staff or is_admin:
        bookings = Booking.objects.all()
        pending_bookings = Booking.objects.filter(status="Pending")
        approved_bookings = Booking.objects.filter(status="Approved")

    # User view: regular users see only their bookings
    elif is_user:
        bookings = Booking.objects.filter(user=request.user)
        pending_bookings, approved_bookings = None, None

    # Employee view: employees see only bookings related to them with statuses Pending and Approved
    elif is_employee:
        pending_bookings = Booking.objects.filter(status="Pending", coach=request.user.username)
        approved_bookings = Booking.objects.filter(status="Approved", coach=request.user.username)
        bookings = None

    # Fallback if user has no specific group or permissions
    else:
        bookings, pending_bookings, approved_bookings = [], [], []

    return render(request, 'bookings/manage_bookings.html', {
        'bookings': bookings,
        'pending_bookings': pending_bookings,
        'approved_bookings': approved_bookings,
        'is_user': is_user,
        'is_employee': is_employee,
        'is_admin': is_admin,
    })

# Create booking view
@login_required
def create_booking(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.status = 'Pending'
        booking.save()
        return redirect('manage_bookings')

    booked_times = Booking.objects.values_list('session_time', flat=True)
    booked_times_list = [dt.strftime("%Y-%m-%dT%H:%M") for dt in booked_times]

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'booked_times_json': json.dumps(booked_times_list)
    })

# Delete booking view (revised)
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    # Allow deletion if the booking belongs to the user or if the user is in the Employees or Admin group
    if booking.user == request.user or request.user.groups.filter(name__in=['Employees', 'Admin']).exists():
        booking.delete()
        messages.success(request, "Booking has been successfully deleted.")
    else:
        messages.error(request, "You do not have permission to delete this booking.")
    return redirect('manage_bookings')

# Booking confirmation view
@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

# Accept booking view for employees/admins
@login_required
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Accepted'
    booking.save()
    return redirect('manage_bookings')

# Approve booking view
@login_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        booking.status = 'Approved' if action == 'approve' else 'Rejected'
        booking.save()
        return redirect('manage_bookings')
    
    return render(request, 'bookings/approve_booking.html', {'booking': booking})

# My account view
@login_required
def my_account(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('my_account')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'bookings/my_account.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

# Mark booking as completed view
@login_required
def mark_completed(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status == 'Approved':
        booking.status = 'Completed'
        booking.save()  
        messages.success(request, "Booking marked as completed.")
    else:
        messages.error(request, "Only approved bookings can be marked as completed.")
    return redirect('manage_bookings')

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Check if the user has permission to edit the booking: owner, staff, superuser, or in "Admin" group
    is_admin = request.user.is_superuser or request.user.is_staff or request.user.groups.filter(name="Admin").exists()
    
    # Debugging: Log user status and permissions for troubleshooting
    print(f"User: {request.user.username}, Superuser: {request.user.is_superuser}, Staff: {request.user.is_staff}, Is Admin Group: {is_admin}")

    # Only allow edit if the user is the booking owner or an admin
    if booking.user != request.user and not is_admin:
        messages.error(request, "You do not have permission to edit this booking.")
        return redirect('manage_bookings')

    # Handle form submission for editing
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking updated successfully.")
            return redirect('manage_bookings')
    else:
        form = BookingForm(instance=booking)

    # Prepare booked times for the datepicker to exclude this booking's slot
    booked_times = Booking.objects.exclude(id=booking.id).values_list('session_time', flat=True)
    booked_times_list = [dt.strftime("%Y-%m-%dT%H:%M") for dt in booked_times]

    return render(request, 'bookings/edit_booking.html', {
        'form': form,
        'booking': booking,
        'booked_times_json': json.dumps(booked_times_list),
    })