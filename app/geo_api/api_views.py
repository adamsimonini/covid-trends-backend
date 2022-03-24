from rest_framework.generics import ListAPIView


from geo_api.serializers import RegionSerializer, ProvinceSerializer, HealthRegionSerializer, WeatherStationSerializer, DiseasesSerializer
from geo_api.models import Region, Province, Health_Region, Weather_Stations, Diseases

class RegionList(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class HealthRegionList(ListAPIView):
    queryset = Health_Region.objects.all()
    serializer_class = HealthRegionSerializer 

class ProvinceList(ListAPIView):
    queryset = Province.objects.all()
    serializer_class =  ProvinceSerializer  

class WeatherStationsList(ListAPIView):
    queryset = Weather_Stations.objects.all()
    serializer_class =  WeatherStationSerializer 

class DiseasesList(ListAPIView):
    queryset = Diseases.objects.all()
    serializer_class = DiseasesSerializer      