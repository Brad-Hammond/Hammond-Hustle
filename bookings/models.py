from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    # Choices for the status of the booking
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  
    feedback = models.TextField(blank=True, null=True)  

    def __str__(self):
        """
        String representation of the Booking instance, showing
        the username, booking date, and status for easy identification.
        """
        return f"{self.user.username} - {self.booking_date} - {self.status}"