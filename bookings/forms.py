# bookings/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Profile  # Import both Booking and Profile models

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session_time', 'coach']  # Include coach in the form
        widgets = {
            'session_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices for 'coach' field based on COACH_CHOICES in Booking model
        self.fields['coach'].choices = Booking.COACH_CHOICES

# Form for employee feedback on a booking
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['feedback']  # Only allow employees to edit the feedback field

# Custom signup form with an optional employee code field
class CustomUserCreationForm(UserCreationForm):
    code = forms.CharField(
        max_length=20, required=False, help_text='Enter your code if you are an employee.'
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'code')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Use the Profile model
        fields = ['first_name', 'last_name', 'phone', 'date_of_birth']  # Include additional fields
