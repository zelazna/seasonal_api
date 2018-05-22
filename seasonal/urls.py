from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='API')

urlpatterns = [
    url(r'^', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('admin/', admin.site.urls),
    url(r'^schema/$', schema_view),
]
