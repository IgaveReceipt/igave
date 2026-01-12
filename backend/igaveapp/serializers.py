from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Receipt


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Generate the default token (access + refresh)
        data = super().validate(attrs)

        # Inject custom user data into the response
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_staff': self.user.is_staff
        }
        return data


class UserSerializer(serializers.ModelSerializer):
    # 1. Explicitly define password so we can make it write_only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # 2. Add 'password' to the fields list
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['id']

    # 3. Override create to Hash the password!
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'], # <--- Hashing happens inside create_user
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user


class ReceiptSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Receipt
        fields = [
            'id',
            'user',
            'store_name',
            'date',
            'total_amount',
            'category',
            'items',
            'status',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']