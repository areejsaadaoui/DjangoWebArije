from django.db import models

from django.utils import timezone
from django.core.exceptions import ValidationError


class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(blank=True, upload_to='prescriptions/')

    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        CONFIRMED = 'Confirmed', 'Confirmed'
        CANCELLED = 'Cancelled', 'Cancelled'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
    )
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(
        'AccountApp.Doctor',
        on_delete=models.CASCADE,
        related_name='appointments',
    )
    patient = models.ForeignKey(
        'AccountApp.Patient',
        on_delete=models.CASCADE,
        related_name='appointments',
    )

    def clean(self):
        modified_date = self._state.adding or (
            Appointment.objects.filter(
                pk=self.pk,appointment_date=self.appointment_date
            ).exists()
        )
        if modified_date and self.appointment_date <= timezone.now():
            raise ValidationError('la date du rendez-vous doit être dans le futur.')
        

    class Meta:
        ordering = ['-appointment_date']
        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unicite_patient-doctor-date',
                violation_error_message='Ce docteur possède déjà un rendez-vous à cette date.',
            )
        ]

    def __str__(self):
        return f"Le rdv est pour la raison {self.reason}"