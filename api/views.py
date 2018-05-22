from rest_framework import viewsets

from api.models import Candidate, Professional, Job
from api.serializers import CandidateSerializer, ProfessionalSerializer, JobSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ProfessionalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
