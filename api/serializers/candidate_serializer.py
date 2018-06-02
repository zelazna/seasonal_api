from api.models import Candidate
from api.serializers import UserSerializer
from api.serializers.base_user_serializer import BaseUserSerializer
from rest_framework import serializers


class CandidateSerializer(BaseUserSerializer):
    job = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Candidate
        fields = (
            'user',
            'year_exp',
            'available_at',
            'profile_view_count',
            'wage_claim',
            'profile_picture_url',
            'description',
            'job'
        )
