from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm  # Import for signup
from .models import Booking
from .forms import BookingForm, FeedbackForm

# Create your views here.
