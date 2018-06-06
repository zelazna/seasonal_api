from api.models import Candidate, Job
from api.serializers import UserSerializer, JobSerializer
from rest_framework import serializers

from api.serializers.mixins.user_serializer_mixin import UserSerializerMixin


class CandidateSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = UserSerializer()
    job_id = serializers.PrimaryKeyRelatedField(source='job', queryset=Job.objects.all(), )

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
            'job',
            'job_id'
        )
        depth = 1
