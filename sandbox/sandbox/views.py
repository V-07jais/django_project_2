from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from core.models import Project

# Homepage
def home(request):
    return render(request, "index.html")   # or homepage.html, choose ONE

# About page
def about(request):
    return render(request, "about.html")   # better than HttpResponse

# Courses list
def courses(request):
    return render(request, "courses.html")  # better than hardcoded HTML

# Single course details
def course_detail(request, courseid):
    return HttpResponse(f"Course ID: {courseid}")   # later replace with template

# Show all projects
def projects(request):
    return render(request, "projects.html")

# Show single project
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "project_detail.html", {"project": project})

# Login
def login_page(request):
    return render(request, "login.html")

# Profile
def profile_page(request):
    return render(request, "profile.html")
