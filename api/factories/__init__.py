from api.models import Job
from .company_factory import CompanyFactory
from .user_factory import UserFactory
from .candidate_factory import CandidateFactory
from .professional_factory import ProfessionalFactory

JOBS = [x for x in Job.objects.all()]
