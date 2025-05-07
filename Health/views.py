from django.shortcuts import render
from .models import Doctor,Patient,Mappings
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from .serializers import DoctorSerializer,PatientSerializer,UserRegisterSerializer,MappingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    def update(self, request, *args, **kwargs):
        if(request.method=='PUT'):
            return super().update(request,partial=True, *args, **kwargs)
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer
    def update(self, request, *args, **kwargs):
        if(request.method=='PUT'):
            return super().update(request,partial=True, *args, **kwargs)

class UserRegisterViewSet(CreateModelMixin,viewsets.GenericViewSet):
    permission_classes = [AllowAny]   # Since we have wrapped all the endpoints for authentication, here we need to allow any user to register
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    
class MappingViewSet(viewsets.ModelViewSet):
    queryset=Mappings.objects.all()
    serializer_class=MappingSerializer
    
    # by default , the retrieve method has the mapping id as the query parameter, but we need to get the patient id so we need to override the retrieve method
    def retrieve(self,request,*args, **kwargs):
        Patient=kwargs['pk']
        mappings=Mappings.objects.select_related('Doctor').filter(Patient=Patient)
        doctors=[mapping.Doctor for mapping in mappings]
        if not doctors:
            return Response({"message":"No mappings found for this patient"},status=404)
        serializer=DoctorSerializer(doctors,many=True)
        return Response(serializer.data)

    
        
        

    
        