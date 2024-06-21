from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model=User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'profile_picture')
        read_only_fields = ['profile_picture']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields = ('id', 'email', 'token', 'password')
        read_only_fields = ['token']
        
class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    profile_picture = serializers.ImageField()
    class Meta:
        model=User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'profile_picture')
        extra_kwargs = {
            'profile_picture': {'required': False}
        }