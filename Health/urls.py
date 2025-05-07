from django.urls import path,include
#import routers
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet,UserRegisterViewSet,MappingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'register', UserRegisterViewSet, basename='user-register')
router.register(r'mappings', MappingViewSet, basename='mappings')

#Defin the URLs
urlpatterns =[
    path('api/',(include(router.urls))),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
]

