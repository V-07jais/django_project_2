"""
URL configuration for sandbox project.
"""

from django.contrib import admin
from django.urls import path, include
from core import views  # keep this if you have sandbox/views.py with homepage etc.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path("login/", views.login_page, name="login_page"),
    path("profile/", views.profile_page, name="profile_page"),
    path('projects/', include('core.urls')),  # ✅ Now core handles /projects/
]
