from django.db import models
from django.contrib.auth.models import User

#Department model
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Specialization models
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('Department',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Doctor Model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


