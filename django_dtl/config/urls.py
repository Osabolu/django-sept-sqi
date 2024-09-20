from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("library/", include("library.urls")),
    # path("authors/", include("authors.urls")),
    # path("views/", include("dtl.urls")),
    # path("", include("pages.urls")),
    path("albums/", include("albums.urls")),
    path("", include("artist.urls")),
]
