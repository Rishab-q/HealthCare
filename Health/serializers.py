from rest_framework import serializers
from .models import Doctor, Patient, Mappings
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    Doctor_info = DoctorSerializer(source='Doctor', read_only=True)
    Patient_info = PatientSerializer(source='Patient', read_only=True)
    class Meta:
        model = Mappings
        fields = ['id', 'Patient', 'Doctor','Doctor_info','Patient_info']
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
 