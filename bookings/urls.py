from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Bookings-related URLs
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('accept_booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('leave_feedback/<int:booking_id>/', views.leave_feedback, name='leave_feedback'),
    path('view_feedback/<int:booking_id>/', views.view_feedback, name='view_feedback'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('bookings/approve/<int:booking_id>/', views.approve_booking, name='approve_booking'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('signup/', views.signup, name='signup'),  # Signup view
]