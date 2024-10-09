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
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    COACH_CHOICES = [
        ('John Doe', 'John Doe'),
        ('Jane Smith', 'Jane Smith'),
        ('Alex Johnson', 'Alex Johnson'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.TextField(blank=True, null=True)
    coach = models.CharField(max_length=100, choices=COACH_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.session_time} - {self.status}"