from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health_regions', views.health_regions, name='health_regions'),
]
