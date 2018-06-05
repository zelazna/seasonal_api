from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^api/v1/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Seasonal API'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
