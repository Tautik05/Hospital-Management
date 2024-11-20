from django.db import models
import uuid
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Patient_profile')
    date_of_birth = models.DateField()
    location = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user.username
