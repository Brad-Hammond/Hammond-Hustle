from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()  # Get the user model

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]

    COACH_CHOICES = [
        ('Brad-Hammond', 'Brad Hammond'),
        ('testemp1', 'Joe Bloggs'),
        ('testemp2Female', 'Jane Doe'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.OneToOneField('Feedback', on_delete=models.SET_NULL, null=True, blank=True, related_name='booking_feedback')  # Link to Feedback model with related_name
    coach = models.CharField(max_length=100, choices=COACH_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.session_time} - {self.status}"

    class Meta:
        permissions = [
            ("can_accept_booking", "Can accept booking"),
            ("can_delete_booking", "Can delete booking"),
        ]


class Feedback(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='feedback_booking')  # Add related_name
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking feedback to a user
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created

    def __str__(self):
        return f"Feedback for {self.booking} by {self.user.username}"

    class Meta:
        permissions = [
            ("can_leave_feedback", "Can leave feedback"),
        ]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)  # Date of Birth field

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
