from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),  # ✅ detail page
    path("login/", views.login_page, name="login_page"),
    path("profile/", views.profile_page, name="profile_page"),
]
