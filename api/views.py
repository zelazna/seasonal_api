from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Candidate, Professional, Job
from api.serializers import CandidateSerializer, ProfessionalSerializer, JobSerializer, CandidateListSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def list(self, request, **kwargs):
        """
        @Override
        Args:
            request: Request object
            **kwargs: TODO

        Returns:
            Response: The Candidates list
        """
        candidates = Candidate.objects.all()
        serializer = CandidateListSerializer(candidates, many=True)
        return Response(serializer.data)


class ProfessionalViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
