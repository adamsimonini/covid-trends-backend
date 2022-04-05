# from rest_framework.exceptions import ValidationError
from xml.dom import ValidationErr
from django.forms import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
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


class HealthRegionList(ListAPIView):
    queryset = HealthRegion.objects.all()
    serializer_class = HealthRegionSerializer 
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('hr_uid', 'fk_province',)
    search_fields = ('name_en', 'name_fr',) 
    pagination_class = ApiPagination

class HealthRegionCreate(CreateAPIView):
    serializer_class = HealthRegionSerializer

    def create(self, request, *args, **kwargs):
        hr_uid = request.data.get('hr_uid')
        if hr_uid is None:
            raise ValidationError({ 'hr_uid': 'Must not be empty' })
        name = request.data.get('name_en')
        if name is None:
            raise ValidationError({ 'name_en': 'Must not be empty' })
        return super().create(request, *args, **kwargs)


class HealthRegionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = HealthRegion.objects.all()
    lookup_field = 'hr_uid'
    serializer_class = HealthRegionSerializer

    def delete(self, request, *args, **kwargs):
        hr_uid = request.data.get('hr_uid')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('HealthRegion_{}'.format(hr_uid))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            HealthRegion = response.data
            cache.set('HealthRegion_{}'.format(HealthRegion['hr_uid']), {
                'name_en': HealthRegion['name_en'],
                'name_fr': HealthRegion['name_fr'],
                'fk_province': HealthRegion['fk_province'],
            })
        return response  

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

class DiseaseCreate(CreateAPIView):
    serializer_class = DiseaseSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name is None:
            raise ValidationError({ 'name': 'Must not be empty' })
        return super().create(request, *args, **kwargs)


class DiseaseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    lookup_field = 'code'
    serializer_class = DiseaseSerializer

    def delete(self, request, *args, **kwargs):
        code = request.data.get('code')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('disease_{}'.format(code))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            disease = response.data
            cache.set('disease_{}'.format(disease['code']), {
                'name': disease['name'],
                'classification': disease['classification'],
                'subclassification': disease['subclassification'],
            })
        return response  


class VaccinationList(ListAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('efficacy_rate', 'percent_pop_vaccinated',)
    search_fields = ('vaccination_name', 'treats_disease',)
    pagination_class = ApiPagination

class VaccinationCreate(CreateAPIView):
    serializer_class = VaccinationSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('vaccination_name')
        if name is None:
            raise ValidationError({ 'vaccination_name': 'Must not be empty' })

        treats_disease = request.data.get('treats_disease')
        if treats_disease is None:
            raise ValidationError({ 'treats_disease': 'Must not be empty' })

        efficacy_rate = request.data.get('efficacy_rate')
        if efficacy_rate is None:
            raise ValidationError({ 'efficacy_rate': 'Must not be empty' })

        return super().create(request, *args, **kwargs)


class VaccinationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Vaccination.objects.all()
    lookup_field = 'code'
    serializer_class = VaccinationSerializer

    def delete(self, request, *args, **kwargs):
        vaccination_name = request.data.get('vaccination_name')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('Vaccination_{}'.format(vaccination_name))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            Vaccination = response.data
            cache.set('Vaccination_{}'.format(Vaccination['vaccination_name']), {
                'treats_disease': Vaccination['treats_disease'],
                'efficacy_rate': Vaccination['efficacy_rate'],
                'percent_pop_vaccinated': Vaccination['percent_pop_vaccinated'],
            })
        return response 