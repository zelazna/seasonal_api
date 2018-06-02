from api.models import Candidate
from api.serializers.base_user_serializer import BaseUserSerializer


class CandidateSerializer(BaseUserSerializer):
    class Meta:
        model = Candidate
        fields = (
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