from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("site-admin/", admin.site.urls),
    path("pages/", include("pages.urls")),
    path("contact/", include("contact.urls")),
]
