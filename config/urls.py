from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("supersecret/", admin.site.urls),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

admin.site.site_header = "Django Next and Docker Admin"
admin.site.site_title = "Django Next and Docker Admin Portal"
admin.site.index_title = "Welcome to the Django Next and Docker Portal"
