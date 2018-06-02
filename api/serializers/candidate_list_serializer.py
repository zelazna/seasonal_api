from api.models import Candidate
from rest_framework import serializers

from api.serializers import UserSerializer


class CandidateListSerializer(serializers.ModelSerializer):
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
