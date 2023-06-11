from rest_framework import serializers
from .models import UserNames

class UserNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNames
        fields = ['id', 'username', 'email', 'description', 'passw']