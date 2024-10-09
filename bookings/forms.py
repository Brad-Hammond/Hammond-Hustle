from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking  # Import the Booking model

# Form for booking creation
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['session_time', 'coach']  # Include coach in the form
        widgets = {
            'session_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# Form for employee feedback on a booking
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['feedback']  # Only allow employees to edit the feedback field

# Custom signup form with employee code field
class CustomUserCreationForm(UserCreationForm):
    code = forms.CharField(max_length=20, required=False, help_text='Enter your code if you are an employee.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'code')