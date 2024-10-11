# bookings/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    COACH_CHOICES = [
        ('Brad Hammond', 'Brad Hammond'),
        ('Joe Bloggs', 'Joe Bloggs'),
        ('Jane Doe', 'Jane Doe'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.TextField(blank=True, null=True)
    coach = models.CharField(max_length=100, choices=COACH_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.session_time} - {self.status}"

    class Meta:
        permissions = [
            ("can_accept_booking", "Can accept booking"),
        ]
