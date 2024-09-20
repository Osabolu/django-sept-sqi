from django.urls import path
from room import views

urlpatterns = [
    path("chatroom/", views.chatroom, name="chatroom"),
]
