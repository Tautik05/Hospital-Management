from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['contact_number', 'specialization']

class DoctorSerializer(serializers.ModelSerializer):
    # Fetching User fields explicitly
    id = serializers.ReadOnlyField(source='user.id')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(source='user.email')

    # Include Doctor-specific fields directly
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'username', 'password' , 'email', 'contact_number', 'specialization']

    def create(self, validated_data):
        # Extract data
        user_data = {
            'username': validated_data['username'],
            'email': validated_data['email'],
            'first_name': validated_data.get('first_name', ''),
            'last_name': validated_data.get('last_name', ''),
            'password': validated_data['password']
        }

        doctor_data = {
            'contact_number': validated_data['contact_number'],
            'specialization': validated_data['specialization']
        }

        # Create User and Doctor profile
        user = User.objects.create_user(**user_data)
        doctor = Doctor.objects.create(user=user, **doctor_data)
        return doctor

    def update(self, instance, validated_data):
        # Update User fields
        user = instance.user
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
        user.save()

        # Update Doctor-specific fields
        instance.contact_number = validated_data.get('contact_number', instance.contact_number)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.save()

        return instance





    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        # read_only_fields = ['id', 'created_at']

class SpecilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name', 'department']
