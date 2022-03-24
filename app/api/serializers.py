from rest_framework import serializers
from api.models import Country, Region, Province, HealthRegion, \
    ForwardSortationArea, WeatherStation, Disease, Vaccination


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'country_code',
            'country_name',
        )


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'name_en',
            'name_fr',
        )


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = (
            'geo_code',
            'alpha_code',
            'name_en',
            'name_fr',
            'fk_region',
            'diseases',
        )


class HealthRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRegion
        fields = (
            'hr_uid',
            'name_en',
            'name_fr',
            'website_en',
            'website_fr',
            'fk_province',
            'diseases',
        )


class ForwardSortationAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForwardSortationArea
        fields = (
            'code',
            'fk_province',
            'diseases',
        )


class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = (
            'code',
            'fk_health_region',
        )


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = (
            'code',
            'name',
            'classification',
            'subclassification',
        )

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = (
            'vaccination_name',
            'treats_disease',
            'efficacy_rate',
            'percent_pop_vaccinated',
        )