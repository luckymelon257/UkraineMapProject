# map_project/urls.py
from django.contrib import admin
from django.urls import path, include  # use include to link to app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map_app.urls')),  # Correctly link to map_app.urls here
]
