from rest_framework import serializers

from api.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        user = User(email=email, password=password)
        user.save()
        instance = self.Meta.model(user, **validated_data)
        instance.save()
        return instance
