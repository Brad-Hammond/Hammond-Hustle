from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Bookings-related URLs
    path('manage_bookings/', views.manage_bookings,
         name='manage_bookings'),
    path('create_booking/', views.create_booking,
         name='create_booking'),
    path('accept_booking/<int:booking_id>/', views.accept_booking,
         name='accept_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking,
         name='delete_booking'),
    path('approve/<int:booking_id>/', views.approve_booking,
         name='approve_booking'),
    path('my_account/', views.my_account,
         name='my_account'),
    path('<int:booking_id>/mark_completed/', views.mark_completed,
         name='mark_completed'),
    path('edit_booking/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),
    path('booking/confirmation/<int:booking_id>/',
         views.booking_confirmation, name='booking_confirmation'),

    # Authentication-related URLs
    path(
        'login/', auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ), name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('signup/', views.signup,
         name='signup'),
]
