from django.db import models

# Create your models here.
class Status(models.TextChoices):
    PENDING = "PENDING", "En attente"
    CONFIRMED = "CONFIRMED", "Confirmé"
    CANCELLED = "CANCELLED", "Annulé"

class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    status = models.CharField(
        max_length=10, 
        choices=Status.choices, 
        default=Status.PENDING
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()