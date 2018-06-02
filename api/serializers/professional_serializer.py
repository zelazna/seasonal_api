from api.models import Professional
from api.serializers.base_user_serializer import BaseUserSerializer


class ProfessionalSerializer(BaseUserSerializer):
    class Meta:
        model = Professional
        fields = ('company',)
