# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("djoser.urls")),  # Note the trailing slash
    path("api/v1/", include("djoser.urls.authtoken")),
    path("api/v1/", include("product.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
