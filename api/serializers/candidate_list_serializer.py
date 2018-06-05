from api.models import Candidate
from rest_framework import serializers

from api.serializers import UserSerializer
from api.serializers.mixins.user_serializer_mixin import UserSerializerMixin


class CandidateListSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidate
        fields = (
            'user',
            'year_exp',
            'available_at',
            'profile_view_count',
            'wage_claim',
            'profile_picture',
            'description',
            'job'
        )
