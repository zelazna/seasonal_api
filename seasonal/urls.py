from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^api/v1/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Seasonal API'))
]
