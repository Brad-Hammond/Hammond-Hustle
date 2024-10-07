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

    # Authentication-related URLs
    path('signup/', views.signup, name='signup'),  # Signup URL
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL
]