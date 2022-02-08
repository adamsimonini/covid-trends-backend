from rest_framework import serializers
from api.models import Health_Region


class HealthRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_Region
        fields = (
            'hr_uid',
            'fk_province_id',
            'name_en',
            'name_fr',
            'website_en',
            'website_fr'
        )
