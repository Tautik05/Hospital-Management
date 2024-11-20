from django.db import models
import uuid
from django.contrib.auth.models import User

class hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class hospitalUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    isAdmin = models.BooleanField(default=False)
    hospital = models.ForeignKey(hospital, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user.username
    
