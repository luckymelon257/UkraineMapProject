# map_app/urls.py
from django.urls import path
from . import views  # This imports views from the correct app (map_app)

urlpatterns = [
    path('generate_map/', views.generate_map, name='generate_map'),
]
