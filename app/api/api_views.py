# from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView #, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import CountrySerializer, RegionSerializer, ProvinceSerializer, HealthRegionSerializer, \
    ForwardSortationAreaSerializer, WeatherStationSerializer, DiseaseSerializer, VaccinationSerializer
from api.models import Country, Region, Province, HealthRegion, \
    ForwardSortationArea, WeatherStation, Disease, Vaccination

class ApiPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('code',)
    search_fields = ('name',)
    pagination_class = ApiPagination


class RegionList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name_en', 'name_fr',)
    pagination_class = ApiPagination


class ProvinceList(ListAPIView):
    queryset = Province.objects.all()
    serializer_class =  ProvinceSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('geo_code',)
    search_fields = ('alpha_code', 'name_en', 'name_fr',) 
    pagination_class = ApiPagination

# class ProvinceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
#     queryset = Province.objects.all()
#     lookup_field = 'geo_code'
#     serializer_class = ProvinceSerializer

#     def delete(self, request, *args, **kwargs):
#         code = request.data.get('geo_code')
#         response = super().delete(request, *args, **kwargs)
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('province_{}'.format(code))
#         return response

#     def update(self, request, *args, **kwargs):
#         response = super().update(request, *args, **kwargs)
#         if response.status_code == 200:
#             from django.core.cache import cache
#             code = response.data
#             cache.dset('geo_code')
#         return response

class HealthRegionList(ListAPIView):
    queryset = HealthRegion.objects.all()
    serializer_class = HealthRegionSerializer 
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('hr_uid', 'fk_province',)
    search_fields = ('name_en', 'name_fr',) 
    pagination_class = ApiPagination


class ForwardSortationAreanList(ListAPIView):
    queryset = ForwardSortationArea.objects.all()
    serializer_class =  ForwardSortationAreaSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('code', 'fk_province',)
    search_fields = ('disease',)
    pagination_class = ApiPagination

 
class WeatherStationList(ListAPIView):
    queryset = WeatherStation.objects.all()
    serializer_class =  WeatherStationSerializer 
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('code',)
    search_fields = ('fk_health_region',)
    pagination_class = ApiPagination


class DiseaseList(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('code',)
    search_fields = ('name',) 
    pagination_class = ApiPagination   


class VaccinationList(ListAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('efficacy_rate', 'percent_pop_vaccinated',)
    search_fields = ('vaccination_name', 'treats_disease',)
    pagination_class = ApiPagination