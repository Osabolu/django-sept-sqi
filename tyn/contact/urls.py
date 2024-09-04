from django.urls import path
from contact import views

urlpatterns = [
    path('contact-us/', views.contact, name='contact'),
    path('about/', views.email, name='email')
]