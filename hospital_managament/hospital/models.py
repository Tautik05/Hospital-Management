from django.db import models
import uuid
from django.contrib.auth.models import User
from patients.models import Patient
from accounts.models import *

class hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    departments = models.ManyToManyField('Department', related_name='departments_available')


    def __str__(self):
        return self.name

class hospitalUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hospital_profile')
    isAdmin = models.BooleanField(default=False)
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user.username
    
class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    

    
