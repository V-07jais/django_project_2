from django.contrib import admin
from .models import Profile, Project

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "skills")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")  
    # ✅ changed posted_by → user




  