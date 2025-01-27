from .models import SMScode
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    confirm_password = serializers.CharField()


    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Пароли не совподают!')

        return data

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise serializers.ValidationError('Такой ник уже есть!')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class SMSCodeSerializers(serializers.Serializer):
    sms_code = serializers.CharField(max_length=100)



