from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DoctorSerializer

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [AllowAny]
    serializer_class = DepartmentSerializer

class SpecilizationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SpecilizationSerializer