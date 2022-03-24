from rest_framework.generics import ListAPIView


from api.serializers import CountrySerializer, RegionSerializer, ProvinceSerializer, HealthRegionSerializer, \
    ForwardSortationArea, WeatherStationSerializer, DiseaseSerializer, VaccinationSerializer
from api.models import Country, Region, Province, HealthRegion, \
    ForwardSortationArea, WeatherStation, Disease, Vaccination

class RegionList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class HealthRegionList(ListAPIView):
    queryset = HealthRegion.objects.all()
    serializer_class = HealthRegionSerializer 

class ProvinceList(ListAPIView):
    queryset = Province.objects.all()
    serializer_class =  ProvinceSerializer  

class WeatherStationList(ListAPIView):
    queryset = WeatherStation.objects.all()
    serializer_class =  WeatherStationSerializer 

class DiseaseList(ListAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer    

class VaccinationList(ListAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer    