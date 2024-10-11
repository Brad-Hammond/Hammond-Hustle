from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Bookings-related URLs
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('create_booking/', views.create_booking, name='create_booking'),
    path('accept_booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('bookings/approve/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('my_account/', views.my_account, name='my_account'),
    path('bookings/<int:booking_id>/mark_completed/', views.mark_completed, name='mark_completed'),

    # Authentication-related URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
