from django.urls import path
# Django URL parameters: https://docs.djangoproject.com/en/4.0/topics/http/urls/
from . import views
from . import api_views

urlpatterns = [
    path('', views.index, name='index'),
    # path('health_regions/', views.all_health_regions, name='get_all_health_regions'),
    # path('health_regions/<hr_uid>/', views.single_health_region_by_hr_uid, name='single_health_region_by_hr_uid'),
    # path('provinces/', views.all_provinces, name='get_all_provincess'),
    # path('provinces/<geo_code>', views.single_province_by_geo_code, name='single_province_by_geo_code'),
    # path('regions/', views.all_regions, name='get_all_regions'),
    # path('forward_sortation_areas/', views.forward_sortation_areas, name='forward_sortation_areas'),
    # path('forward_sortation_areas/<str:fsa>', views.single_forward_sortation_area, name='single_forward_sortation_area'),
    # path('weather_stations/', views.all_weather_stations, name='get_all_weather_stations'),
    # path('diseases/', views.all_diseases, name='get_all_diseases'),

    # List Views
    path('country/', api_views.CountryList.as_view(), name='country'),
    path('region/', api_views.RegionList.as_view(), name='region'),
    path('health_region/', api_views.HealthRegionList.as_view(), name='health_region'),
    path('disease/', api_views.DiseaseList.as_view(), name='disease'),
    path('weatherstation/', api_views.WeatherStationList.as_view(), name='weatherstation'),
    path('province/', api_views.ProvinceList.as_view(), name='province'),
    path('vaccination/', api_views.VaccinationList.as_view(), name='vaccination'),

    # Create Views
    path('health_region/new', api_views.HealthRegionCreate.as_view()),
    path('disease/new', api_views.DiseaseCreate.as_view()),
    path('vaccination/new', api_views.VaccinationCreate.as_view()),

    # Update / Delete Views
    path('health_region/<int:hr_uid>', api_views.HealthRegionRetrieveUpdateDestroy.as_view()),
    path('disease/<int:code>', api_views.DiseaseRetrieveUpdateDestroy.as_view()),
    path('vaccination/<str:vaccination_name>', api_views.VaccinationRetrieveUpdateDestroy.as_view()),

]
