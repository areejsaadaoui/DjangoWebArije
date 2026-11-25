from django.contrib import admin
from .models import Appointment

# Register your models here.
#admin.site.register(Appointment) : enregistre mais ne te permet pas de personnaliser l'affichage dans l'interface d'administration
@admin.register(Appointment) #enregistrement de la classe Appointment dans l'interface d'administration
class AppointmentAdminPers(admin.ModelAdmin):
    pass