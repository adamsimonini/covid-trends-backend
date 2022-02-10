from django.db import models
from django.contrib.postgres.fields import ArrayField
# standard geographical classification code https://en.wikipedia.org/wiki/Standard_Geographical_Classification_code_(Canada)
# ORM docs: https://docs.djangoproject.com/en/4.0/topics/db/models/
# fields reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types
# Model meta options: https://docs.djangoproject.com/en/4.0/ref/models/options/


class Region(models.Model):
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)

    class Meta:
        app_label = 'geo_api'
        db_table = 'region'


class Province(models.Model):
    geo_code = models.PositiveSmallIntegerField(blank=False)  # standard geographical classification code
    alpha_code = models.CharField(max_length=2, blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    fk_region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'geo_api'
        db_table = 'province'


class Health_Region(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    website_en = models.CharField(max_length=300, blank=False)
    website_fr = models.CharField(max_length=300, blank=False)
    fk_province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'geo_api'
        db_table = 'health_region'


class Forward_Sortation_Area(models.Model):
    code = models.CharField(max_length=3, blank=False)  # first 3 digits of a postal code
    health_regions = ArrayField(models.PositiveSmallIntegerField(blank=False))  # an fsa can contain multiple health regions (i.e., 1, 2, or even 3)

    class Meta:
        app_label = 'geo_api'
        db_table = 'forward_sortation_area'
