from django.urls import path
from . import views

app_name = "page"

urlpatterns = [
    path("server/", views.services, name="services"),
    path("test/", views.testimonials, name="testimonials"),
    path("case/", views.case_study, name="case_study"),
    path("blog/", views.blog, name="blog"),
    path("price/", views.pricing, name="pricing"),
]
