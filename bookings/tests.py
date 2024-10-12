from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Booking, Profile, Feedback
from .forms import (
    BookingForm,
    FeedbackForm,
    CustomUserCreationForm,
    UserUpdateForm,
    ProfileUpdateForm,
)
from datetime import datetime, timedelta

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user1', password='password123')
        self.employee = User.objects.create_user(username='employee1', password='password123')
        self.admin = User.objects.create_superuser(username='admin1', password='password123')

        users_group = Group.objects.create(name="Users")
        employees_group = Group.objects.create(name="Employees")
        admins_group = Group.objects.create(name="Admin")
        
        self.user.groups.add(users_group)
        self.employee.groups.add(employees_group)
        self.admin.groups.add(admins_group)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_signup_view(self):
        response = self.client.post(reverse('signup'), {
            'username': 'testuser',
            'password1': 'password12345',
            'password2': 'password12345',
            'code': ''
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_manage_bookings_user(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('manage_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')
        self.assertTrue(response.context['is_user'])

    def test_manage_bookings_employee(self):
        self.client.login(username='employee1', password='password123')
        response = self.client.get(reverse('manage_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')
        self.assertTrue(response.context['is_employee'])

    def test_manage_bookings_admin(self):
        self.client.login(username='admin1', password='password123')
        response = self.client.get(reverse('manage_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/manage_bookings.html')
        self.assertTrue(response.context['is_admin'])

    def test_create_booking_view(self):
        self.client.login(username='user1', password='password123')
        session_time = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")
        response = self.client.post(reverse('create_booking'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'dob': '2000-01-01',
            'coach': self.employee.username,
            'session_time': session_time
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Booking.objects.filter(user=self.user).exists())

    def test_delete_booking_view(self):
        self.client.login(username='user1', password='password123')
        booking = Booking.objects.create(user=self.user, session_time=datetime.now() + timedelta(days=1))
        response = self.client.post(reverse('delete_booking', args=[booking.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())

    def test_booking_confirmation_view(self):
        booking = Booking.objects.create(user=self.user, session_time=datetime.now() + timedelta(days=1))
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('booking_confirmation', args=[booking.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_confirmation.html')

    def test_approve_booking_view(self):
        self.client.login(username='employee1', password='password123')
        booking = Booking.objects.create(user=self.user, session_time=datetime.now() + timedelta(days=1), status="Pending")
        response = self.client.post(reverse('approve_booking', args=[booking.id]), {'action': 'approve'})
        booking.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(booking.status, 'Approved')

    def test_mark_completed_view(self):
        booking = Booking.objects.create(user=self.user, session_time=datetime.now() + timedelta(days=1), status="Approved")
        self.client.login(username='employee1', password='password123')
        response = self.client.post(reverse('mark_completed', args=[booking.id]))
        booking.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(booking.status, 'Completed')

    def test_edit_booking_view(self):
        booking = Booking.objects.create(user=self.user, session_time=datetime.now() + timedelta(days=1))
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('edit_booking', args=[booking.id]), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'phone': '9876543210',
            'dob': '1995-05-05',
            'coach': self.employee.username,
            'session_time': (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M")
        })
        booking.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(booking.user, self.user)


class FormTests(TestCase):
    def test_booking_form_valid(self):
        form = BookingForm(data={
            'session_time': (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M"),
            'coach': 'Brad-Hammond'
        })
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid(self):
        form = BookingForm(data={'session_time': 'invalid_date'})
        self.assertFalse(form.is_valid())

    def test_feedback_form_valid(self):
        form = FeedbackForm(data={'feedback_text': 'Great session!'})
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_valid(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'code': 'EMPLOYEE2024'
        })
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_password_mismatch(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'differentpassword'
        })
        self.assertFalse(form.is_valid())

    def test_user_update_form(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        form = UserUpdateForm(data={'username': 'newusername', 'email': 'new@example.com'}, instance=user)
        self.assertTrue(form.is_valid())

    def test_profile_update_form(self):
        user = User.objects.create_user(username='testuser')
        profile = Profile.objects.create(user=user)
        form = ProfileUpdateForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'date_of_birth': '2000-01-01'
        }, instance=profile)
        self.assertTrue(form.is_valid())
