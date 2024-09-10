from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("library/", include("library.urls")),
    path("authors/", include("authors.urls")),
    path("views/", include("dtl.urls")),
]
