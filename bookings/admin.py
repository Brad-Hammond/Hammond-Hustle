from django.contrib import admin
from .models import Booking, Profile

# Register the Booking model
admin.site.register(Booking)

# Register the Profile model with custom admin settings
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'date_of_birth')  # Specify fields to display
    search_fields = ('user__username', 'first_name', 'last_name')  # Enable search by username, first or last name

admin.site.register(Profile, ProfileAdmin)  # Register Profile model with the admin interface
