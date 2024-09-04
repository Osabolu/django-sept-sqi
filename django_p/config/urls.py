
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("site-admin/", admin.site.urls),
    path('chatroom/', include('room.urls')),
    path('contact/', include('contact.urls')),
   
]
