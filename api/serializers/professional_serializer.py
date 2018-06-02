from rest_framework import serializers

from api.models import Professional, User, Company
from api.serializers import UserSerializer, CompanySerializer


class ProfessionalSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    user = UserSerializer()

    class Meta:
        model = Professional
        fields = ('user', 'company')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        company_data = validated_data.pop('company')
        user = User.objects.create(**user_data)
        company = Company.objects.create(**company_data)
        return Professional.objects.create(user=user, company=company, **validated_data)
