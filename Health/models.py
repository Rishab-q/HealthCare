from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class SexChoices(models.TextChoices):
    MALE='Male','Male'
    FEMALE='Female','Female'
    OTHERS='Others','Others'

class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    Sex=models.CharField(max_length=10,choices=SexChoices.choices)
    Qualification=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    contact=PhoneNumberField(max_length=15,null=True)
    email=models.EmailField(null=True,blank=True)   
    def __str__(self):
        return self.Name
    
class Patient(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=10,choices=SexChoices.choices)
    contact=PhoneNumberField(max_length=15,null=True)
    def __str__(self):
        return self.Name
    

class Mappings(models.Model):
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.Patient.Name} - {self.Doctor.Name}"
