from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)
router.register(r'professionals', views.ProfessionalViewSet)
router.register(r'jobs', views.JobViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]
