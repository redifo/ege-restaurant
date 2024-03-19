from django.db import models
from reservations.models import Reservation


class EmailTemplate(models.Model):
    """
    model stores predefined email templates
    """
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name

class Email(models.Model):
    """
    model represents individual emails to be sent
    """
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient}"

class ReservationEmail(models.Model):
    """
    model links a reservation to an email
    """
    reservation = models.OneToOneField('reservations.Reservation', on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name="reservations_email")

    def __str__(self):
        return f"Email for Reservation {self.reservation}"
