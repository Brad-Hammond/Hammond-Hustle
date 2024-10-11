from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test  # Import user_passes_test here
from django.contrib.auth.models import Group
from .models import Booking, Profile
from .forms import BookingForm, CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm  # Import your forms here
from django.contrib import messages
import json

# Create your views here.

@login_required
def booking_page(request):
    return render(request, 'booking.html')

# View to render base.html for the home/root URL
def home(request):
    is_user = request.user.is_authenticated and request.user.groups.filter(name='Users').exists()
    return render(request, 'base.html', {'is_user': is_user})

# View for user signup
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

@login_required
def manage_bookings(request):
    is_user = request.user.groups.filter(name="Users").exists()
    is_employee = request.user.groups.filter(name="Employees").exists()

    if is_user:
        bookings = Booking.objects.filter(user=request.user)
        pending_bookings, approved_bookings = None, None
    elif is_employee:
        pending_bookings = Booking.objects.filter(status="Pending", coach=request.user.username)
        approved_bookings = Booking.objects.filter(status="Approved", coach=request.user.username)
        bookings = None
    else:
        bookings, pending_bookings, approved_bookings = [], [], []

    return render(request, 'bookings/manage_bookings.html', {
        'bookings': bookings,
        'pending_bookings': pending_bookings,
        'approved_bookings': approved_bookings,
        'is_user': is_user,
        'is_employee': is_employee,
    })

@login_required
def create_booking(request):
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.status = 'Pending'
        booking.save()
        return redirect('manage_bookings')

    existing_bookings = Booking.objects.filter(user=request.user)
    booked_times = Booking.objects.values_list('session_time', flat=True)
    booked_times_list = [dt.strftime("%Y-%m-%dT%H:%M") for dt in booked_times]

    return render(request, 'bookings/create_booking.html', {
        'form': form,
        'existing_bookings': existing_bookings,
        'booked_times_json': json.dumps(booked_times_list)
    })

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})

@login_required
@permission_required('bookings.can_accept_booking', raise_exception=True)
def accept_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'Accepted'
    booking.save()
    return redirect('manage_bookings')

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user == request.user or request.user.groups.filter(name__in=['Employees', 'Admin']).exists():
        booking.delete()
        return redirect('manage_bookings')
    else:
        return redirect('manage_bookings')

@login_required
@permission_required('bookings.can_accept_booking', raise_exception=True)
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        booking.status = 'Approved' if action == 'approve' else 'Rejected'
        booking.save()
        return redirect('manage_bookings')
    
    return render(request, 'bookings/approve_booking.html', {'booking': booking})

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

@login_required
@user_passes_test(lambda u: u.is_staff or u.groups.filter(name='Admin').exists())
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user == request.user or request.user.groups.filter(name__in=['Admin']).exists():
        booking.delete()
        messages.success(request, "Booking has been successfully deleted.")
    else:
        messages.error(request, "You do not have permission to delete this booking.")
    return redirect('manage_bookings')

@login_required
@permission_required('bookings.can_accept_booking', raise_exception=True)
def mark_completed(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.status == 'Approved':
        booking.status = 'Completed'
        booking.save()  
        messages.success(request, "Booking marked as completed.")
        return redirect('manage_bookings')
    else:
        messages.error(request, "Only approved bookings can be marked as completed.")
        return redirect('manage_bookings')
