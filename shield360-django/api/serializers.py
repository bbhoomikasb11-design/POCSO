from rest_framework import serializers
from .models import User, Module, Progress, Report, Alert, ChatbotMessage
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'age']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True, required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'age', 'name']
    def validate_password(self, value):
        validate_password(value)
        return value
    def create(self, validated_data):
        password = validated_data.pop('password')
        name = validated_data.pop('name', '')
        # auto-derive username from email if not provided
        if not validated_data.get('username'):
            validated_data['username'] = (validated_data.get('email') or '').split('@')[0]
        user = User(**validated_data)
        if name:
            parts = name.strip().split(' ', 1)
            user.first_name = parts[0]
            if len(parts) > 1:
                user.last_name = parts[1]
        user.set_password(password)
        user.save()
        return user

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class ChatbotMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotMessage
        fields = '__all__'

