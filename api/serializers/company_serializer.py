from rest_framework import serializers

from api.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'address', 'job')

    def create(self, validated_data):
        return Company.objects.create(**validated_data)
