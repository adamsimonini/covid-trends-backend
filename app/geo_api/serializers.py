from rest_framework import serializers
from geo_api.models import Region, Province, Health_Region


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
            'fk_region_id',
        )


class HealthRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Region
        fields = (
            'hr_uid',
            'name_en',
            'name_fr',
            'website_en',
            'website_fr',
            'fk_province_id',
        )
