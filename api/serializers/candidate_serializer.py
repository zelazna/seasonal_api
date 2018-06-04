from api.models import Candidate
from api.serializers import UserSerializer
from rest_framework import serializers

from api.serializers.mixins.user_serializer_mixin import UserSerializerMixin


class CandidateSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = UserSerializer()

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
