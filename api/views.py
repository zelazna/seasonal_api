from rest_framework import viewsets, mixins, generics
from rest_framework.parsers import MultiPartParser, FormParser

from api.models import Candidate, Professional, Job
from api.permissions import IsOwnerOrReadOnly, IsProfessional
from api.serializers import CandidateSerializer, ProfessionalSerializer, JobSerializer
from django.db.models import F

from rest_framework.response import Response


class CandidateList(mixins.ListModelMixin, mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (IsOwnerOrReadOnly, IsProfessional)

    def get(self, request):
        queryset = Candidate.objects.all()
        job_name = request.query_params.get('job_name', None)
        if job_name is not None:
            queryset = queryset.filter(job__name=job_name)
        serializer = CandidateSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CandidateDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      generics.GenericAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    # TODO : fix auth token not handled with multipart/form-data
    # permission_classes = (IsOwnerOrReadOnly,)
    parser_classes = (MultiPartParser, FormParser)

    def retrieve(self, request, *args, **kwargs):
        """
        Increment the profile views
        Args:
            request: Request object
            *args: TBD
            **kwargs: TBD

        Returns:
            Response
        """
        instance = self.get_object()
        # https://docs.djangoproject.com/en/2.0/ref/models/instances/#updating-attributes-based-on-existing-fields
        instance.profile_view_count = F('profile_view_count') + 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if request.FILES.get('file'):
            instance = self.get_object()
            instance.profile_picture = request.FILES['file']
            instance.save()
        return self.partial_update(request, *args, **kwargs)


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
