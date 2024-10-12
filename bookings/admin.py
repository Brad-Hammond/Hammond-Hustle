from django.contrib import admin
from .models import Booking, Profile, Feedback

# Register the Booking model
admin.site.register(Booking)
admin.site.register(Feedback)

# Register the Profile model with custom admin settings
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name', 'last_name', 'phone', 'date_of_birth'
    )
    search_fields = ('user__username', 'first_name', 'last_name')


admin.site.register(Profile, ProfileAdmin)
