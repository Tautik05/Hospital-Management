from rest_framework.viewsets import ModelViewSet
from .models import hospital
from .serializers import *
from rest_framework.permissions import AllowAny

class HospitalViewSet(ModelViewSet):
    queryset = hospital.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HospitalSerializer

class HospitalUserViewSet(ModelViewSet):
    queryset = hospitalUserProfile.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HospitalUserSerializer

