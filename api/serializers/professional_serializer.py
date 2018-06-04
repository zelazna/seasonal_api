from rest_framework import serializers

from api.models import Professional, User, Company
from api.serializers import UserSerializer, CompanySerializer
from api.serializers.mixins.user_serializer_mixin import UserSerializerMixin


class ProfessionalSerializer(UserSerializerMixin, serializers.ModelSerializer):
    company = CompanySerializer()
    user = UserSerializer()

    class Meta:
        model = Professional
        fields = ('user', 'company')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User(**user_data)
        if password is not None:
            user.set_password(password)
        user.save()
        company_data = validated_data.pop('company')
        company = Company.objects.create(**company_data)
        return Professional.objects.create(user=user, company=company, **validated_data)
