from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Candidate, Professional, Job
from api.permissions import IsOwnerOrReadOnly, IsProfessional
from api.serializers import CandidateSerializer, ProfessionalSerializer, JobSerializer, CandidateListSerializer
from django.db.models import F


class CandidateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (IsOwnerOrReadOnly, IsProfessional)

    def retrieve(self, request, *args, **kwargs):
        # https://docs.djangoproject.com/en/2.0/ref/models/instances/#updating-attributes-based-on-existing-fields
        candidate = self.get_object()
        candidate.profile_view_count = F('profile_view_count') + 1
        candidate.save()
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, **kwargs):
        """
        @Override
        Args:
            request: Request object
            **kwargs: TODO

        Returns:
            Response: The Candidates list
        """
        queryset = Candidate.objects.all()
        job_name = self.request.query_params.get('job_name', None)
        if job_name is not None:
            queryset = queryset.filter(job__name=job_name)
        serializer = CandidateListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfessionalViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
