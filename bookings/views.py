from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm  # Import for signup
from .models import Booking
from .forms import BookingForm, FeedbackForm, CustomUserCreationForm

# Create your views here.

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
    
    return render(request, 'accounts/signup.html', {'form': form})

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
