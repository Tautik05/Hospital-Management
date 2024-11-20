from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospitalUserProfile
        fields = ['isAdmin', 'hospital', 'phone_number', 'uuid']


class HospitalUserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')

        user = User.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        # Create or update the user profile
        hospitalUserProfile.objects.update_or_create(
            user=user,
            defaults=profile_data
        )

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)

        # Update the main user fields
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()

        # Update the user profile
        if profile_data:
            hospitalUserProfile.objects.update_or_create(
                user=instance,
                defaults=profile_data
            )

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            profile_data = UserProfileSerializer(instance.profile).data
            representation['profile'] = profile_data
        except hospitalUserProfile.DoesNotExist:
            representation['profile'] = None
        return representation


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = hospital
        fields = ['id', 'name', 'address', 'phone_number', 'email', 'created_at', 'departments']
        read_only_fields = ['id', 'created_at']