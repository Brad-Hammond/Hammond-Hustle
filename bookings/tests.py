from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.utils import timezone
from .models import Booking, Profile, Feedback
from .forms import (
    BookingForm, FeedbackForm, CustomUserCreationForm,
    UserUpdateForm, ProfileUpdateForm,
)
from datetime import datetime, timedelta


class ViewTests(TestCase):
    def setUp(self):
        # Setting up test client, users, and user groups for test cases
        self.client = Client()
        self.user = User.objects.create_user(
            username='user1', password='password123'
        )
        self.employee = User.objects.create_user(
            username='employee1', password='complex_password_2024!'
        )
        self.admin = User.objects.create_superuser(
            username='admin1', password='complex_password_2024!'
        )

        # Create user groups and assign users to groups
        users_group = Group.objects.create(name="Users")
        employees_group = Group.objects.create(name="Employees")
        admins_group = Group.objects.create(name="Admin")
        self.user.groups.add(users_group)
        self.employee.groups.add(employees_group)
        self.admin.groups.add(admins_group)

    def test_signup_view(self):
        # Testing user signup view to ensure it works correctly
        # Expected outcome: user is created, and response redirects
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'complex_password_2024!',
            'password2': 'complex_password_2024!',
            'code': ''  # 'code' is optional or specific codes can be tested
        })
        if response.status_code == 200:
            print(response.context['form'].errors)
        self.assertEqual(response.status_code, 302)

    def test_create_booking_view(self):
        # Testing booking creation view with valid data
        # Expected outcome: booking is created, response redirects
        self.client.login(username='user1', password='password123')
        session_time = timezone.make_aware(datetime.now() + timedelta(days=1))
        response = self.client.post(reverse('create_booking'), {
            'first_name': 'John', 'last_name': 'Doe',
            'email': 'john@example.com', 'phone': '1234567890',
            'dob': '2000-01-01', 'coach': 'Brad-Hammond',
            'session_time': session_time.strftime("%Y-%m-%dT%H:%M")
        })
        if response.status_code == 200:
            print(response.context['form'].errors)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user).exists())

    def test_edit_booking_view(self):
        # Testing booking edit view to ensure booking can be modified
        # Expected outcome: booking is updated, and response redirects
        booking = Booking.objects.create(
             user=self.user, session_time=timezone.now() + timedelta(days=1)
        )
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('edit_booking', args=[booking.id]), {
            'first_name': 'Jane', 'last_name': 'Doe',
            'email': 'jane@example.com', 'phone': '9876543210',
            'dob': '1995-05-05', 'coach': 'Brad-Hammond',
            'session_time': (timezone.make_aware(
                datetime.now() + timedelta(days=2))
            ).strftime("%Y-%m-%dT%H:%M")
        })
        
        if response.status_code == 200:
            print(response.context['form'].errors)
        
        booking.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(booking.user, self.user)
