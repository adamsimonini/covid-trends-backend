from django.urls import path
# Django URL parameters: https://docs.djangoproject.com/en/4.0/topics/http/urls/
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health_regions', views.get_all_health_regions, name='health_regions'),
    path('forward_sortation_areas', views.forward_sortation_areas, name='forward_sortation_areas'),
    path('forward_sortation_areas/<str:fsa>', views.single_forward_sortation_area, name='single_forward_sortation_area'),
    path('all_hr/', views.get_all_health_regions, name='get_all_hr')
]
