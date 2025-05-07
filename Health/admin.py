from django.contrib import admin
from .models import Doctor, Patient, Mappings
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.fields]
    
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.fields]
    
@admin.register(Mappings)
class MappingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mappings._meta.fields]