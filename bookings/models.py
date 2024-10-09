from django.db import models
from django.contrib.auth import get_user_model

# Get the custom or default User model
User = get_user_model()

class Coach(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(User, related_name="assigned_coaches")

    def __str__(self):
        return self.name

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
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String representation of the Booking instance, showing
        the username, booking date, and status for easy identification.
        """
        return f"{self.user.username} - {self.session_time} - {self.status}"
