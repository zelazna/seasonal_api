from rest_framework import serializers

from api.models import Professional
from api.serializers import UserSerializer
from api.serializers.base_user_serializer import BaseUserSerializer


class ProfessionalSerializer(BaseUserSerializer):
    company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Professional
        fields = ('user', 'company',)
