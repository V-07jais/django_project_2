from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project





# Homepage (Project Feed)
def index(request):
    return render(request, "index.html")


# Signup/Login Page
def login_page(request):
    return render(request, "login.html")


# Profile Page
def profile_page(request):
    return render(request, "profile.html")


# Add Project Page
def projects(request):
    return render(request, "projects.html")


# Project list (all projects)
def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, "project_list.html", {"projects": projects})


# Project detail page
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "project_detail.html", {"project": project})


