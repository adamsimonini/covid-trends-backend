# https://docs.djangoproject.com/en/4.0/ref/models/querysets/

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from backend_api.models import Country, Region, Province, HealthRegion, \
    ForwardSortationArea, WeatherStation, Disease, Vaccination
from backend_api.serializers import CountrySerializer, RegionSerializer, ProvinceSerializer, HealthRegionSerializer, \
    ForwardSortationArea, WeatherStationSerializer, DiseaseSerializer, VaccinationSerializer
from rest_framework.decorators import api_view

# health region endpoints


@api_view(['GET'])
def all_health_regions(request):
    health_regions = HealthRegion.objects.all()
    health_region_serializer = HealthRegionSerializer(health_regions, many=True)
    return JsonResponse(health_region_serializer.data, safe=False)


@api_view(['GET'])
def single_health_region_by_hr_uid(request, hr_uid):
    health_region = HealthRegion.objects.get(hr_uid=hr_uid)
    health_region_serializer = HealthRegionSerializer(health_region, many=False)
    return JsonResponse(health_region_serializer.data, safe=False)

# province endpoints


@api_view(['GET'])
def all_provinces(request):
    provinces = Province.objects.all()
    province_serializer = ProvinceSerializer(provinces, many=True)
    return JsonResponse(province_serializer.data, safe=False)


@api_view(['GET'])
def single_province_by_geo_code(request, geo_code):
    province = Province.objects.get(geo_code=geo_code)
    province_serializer = ProvinceSerializer(province, many=False)
    return JsonResponse(province_serializer.data, safe=False)

# region endpoints


@api_view(['GET'])
def all_regions(request):
    regions = Region.objects.all()
    region_serializer = RegionSerializer(regions, many=True)
    return JsonResponse(region_serializer.data, safe=False)

@api_view(['GET'])
def all_weather_stations(request):
    weather_stations = WeatherStation.objects.all()
    weather_station_serializer = WeatherStationSerializer(weather_stations, many=True)
    return JsonResponse(weather_station_serializer.data, safe=False)

@api_view(['GET'])
def all_diseases(request):
    diseases = Disease.objects.all()
    diseases_serializer = DiseaseSerializer(diseases, many=True)
    return JsonResponse(diseases_serializer.data, safe=False)


def index(request):
    return HttpResponse('''
        Welcome to the Public Health Trends API. Current endpoints in development:
        \n 1) health_regions/ (retrieve all health regions)
        \n 2) forward_sortation_areas/ (retrieve all FSAs)
        \n 3) single_forward_sortation_area/ (retrieve a single FSA by its 3-character code)
    ''')


# @api_view(['GET'])
# def health_regions(request):
#     data = {
#         'health_regions': [
#             {
#                 'id': '1110',
#                 'name_en': 'Toronto Health',
#                 'name_fr': 'Toronto Health',
#                 'website_en': 'https://www.toronto.ca/community-people/health-wellness-care/',
#                 'website_fr': 'https://www.toronto.ca/community-people/health-wellness-care/'
#             },
#             {
#                 'id': '595',
#                 'name_en': 'Laval Health',
#                 'name_fr': 'Laval Health',
#                 'website_en': 'https://www.lavalensante.com/en/covid19/',
#                 'website_fr': 'https://www.lavalensante.com/covid19/'
#             },
#             {
#                 'id': '2406',
#                 'name_en': 'Vancouver Health',
#                 'name_fr': 'Vancouver Health',
#                 'website_en': 'http://www.vch.ca/covid-19',
#                 'website_fr': 'http://www.vch.ca/covid-19'
#             },
#             {
#                 'id': '499',
#                 'name_en': 'Halifax Health',
#                 'name_fr': 'Halifax Health',
#                 'website_en': 'https://novascotia.ca/coronavirus/',
#                 'website_fr': 'https://novascotia.ca/coronavirus/'
#             }
#         ]
#     }
#     return JsonResponse(data)


def forward_sortation_areas(request):
    data = {
        'forward_sortation_areas': [
            {
                'id': '1',
                'fsa': 'A0A',
                'health_regions': '1011',
                'estimated_pop': '8631',
            },
            {
                'id': '2',
                'fsa': 'A0B',
                'health_regions': '1011',
                'estimated_pop': '3066',
            },
            {
                'id': '3',
                'fsa': 'A0C',
                'health_regions': '1011',
                'estimated_pop': '32',
            },
            {
                'id': '4',
                'fsa': 'A0D',
                'health_regions': '1011',
                'estimated_pop': '1242',
            }
        ]
    }
    return JsonResponse(data)


def single_forward_sortation_area(request, fsa):
    data = {
        'id': 1,
        'fsa': fsa,
        'health_regions': '1011',
        'estimated_pop': '8631'
    }
    return JsonResponse(data)
