from rest_framework import serializers
from api.models import Candidate, Professional, Job


class BaseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class CandidateSerializer(BaseSerializer):
    class Meta:
        model = Candidate
        fields = (
            'id',
            'email',
            'password',
            'year_exp',
            'available_at',
            'profile_view_count',
            'wage_claim',
            'profile_picture_url',
            'description',
            'job'
        )


class ProfessionalSerializer(BaseSerializer):
    class Meta:
        model = Professional
        fields = ('company',)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name',)
