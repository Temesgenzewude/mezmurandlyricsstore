
from rest_framework import serializers
from .models import CustomUser


class CustomUserCreationSerializer(serializers.ModelSerializer):
    username=serializers.EmailField(max_length=100)
    fullname=serializers.CharField(max_length=50)
    password=serializers.CharField(min_length=6, write_only=True)
    
    
    class Meta:
        model=CustomUser
        fields =["username", "fullname", "password"]
        
    
    def validate(self, attrs):
        username_exists=CustomUser.objects.filter(username=attrs["username"]).exists()
        
        if username_exists:
            raise serializers.ValidationError(detail="User with this username exists")
        
        return super().validate(attrs) 
        
    