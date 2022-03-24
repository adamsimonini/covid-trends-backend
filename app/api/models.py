from django.db import models
from django.contrib.postgres.fields import ArrayField
# standard geographical classification code https://en.wikipedia.org/wiki/Standard_Geographical_Classification_code_(Canada)
# ORM docs: https://docs.djangoproject.com/en/4.0/topics/db/models/
# fields reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types
# Model meta options: https://docs.djangoproject.com/en/4.0/ref/models/options/

### api_fixture.json model refers to lowercase class name and not db_table variable name

# To control all the geo related choices made
class GeoChoiceSelection():

    CHOICES = [
        ('Atlantic', 'Newfoundland and Labrador', 'NL', '10'), 
        ('Atlantic', 'Prince Edward Island', 'PE', '11'), 
        ('Atlantic', 'Nova Scotia', 'NS', '12'), 
        ('Atlantic', 'New Brunswick', 'NB', '13'), 
        ('Quebec', 'Quebec', 'QC', '24'), 
        ('Ontario', 'Ontario', 'ON', '35'), 
        ('Prairies', 'Manitoba', 'MB', '46'), 
        ('Prairies', 'Saskatchewan', 'SK', '47'), 
        ('Prairies', 'Alberta', 'AB', '48'), 
        ('British Columbia', 'British Columbia', 'BC', '59'), 
        ('Territories', 'Yukon', 'YT', '60'), 
        ('Territories', 'Northwest Territories', 'NT', '61'),
    ]

    def get_choices(subject, choices=CHOICES):

        # Based on the subject of the choices, changes the index of the each item in CHOICES
        # to look through when iterating through to pull "the choice" at the first specified index
        # and "the result" which is the Province name at a constant index 1 
        subjects = {'GEO_CODE': [3, 1], 'ALPHA_CODE': [2, 1], 'REGION_CHOICES': [0, 1]}

        if subject in subjects:
            return [(x[subjects[subject][0]], x[subjects[subject][1]]) for x in choices]
            
        return ValueError('Unrecognized choice subject')


class Country(models.Model):
    code = models.PositiveSmallIntegerField(blank=False)
    name = models.CharField(max_length=150, blank=False)

    class Meta:
        app_label = 'api'
        db_table = 'country'


class Region(models.Model):
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)

    class Meta:
        app_label = 'api'
        db_table = 'region'


class Province(models.Model):
    # geo_code = models.PositiveSmallIntegerField(blank=False)  # standard geographical classification code
    # alpha_code = models.CharField(max_length=2, blank=False)
    geo_code = models.CharField(max_length=2, choices=GeoChoiceSelection.get_choices('GEO_CODE'), blank=False)
    alpha_code = models.CharField(max_length=2, choices=GeoChoiceSelection.get_choices('ALPHA_CODE'), blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    fk_region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE
    )
    disease = models.ManyToManyField('Disease', blank=True)

    class Meta:
        app_label = 'api'
        db_table = 'province'


class HealthRegion(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    website_en = models.CharField(max_length=300, blank=False)
    website_fr = models.CharField(max_length=300, blank=False)
    fk_province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE
    )
    disease = models.ManyToManyField('Disease', blank=True)

    class Meta:
        app_label = 'api'
        db_table = 'health_region'


class ForwardSortationArea(models.Model):
    code = models.CharField(max_length=3, blank=False)  # first 3 digits of a postal code

    # The below is not always true since we cannot directly correlate HR and FSA since neither is the true parent or child of another
    # Therefore, we will need to simply connect FSA and HR both to Province seperately
    # health_regions = ArrayField(models.PositiveSmallIntegerField(blank=False))  # an fsa can contain multiple health regions (i.e., 1, 2, or even 3)
    
    fk_province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE
    )
    disease = models.ManyToManyField('Disease', blank=True)

    class Meta:
        app_label = 'api'
        db_table = 'forward_sortation_area'


class WeatherStation(models.Model):
    code = models.PositiveSmallIntegerField(blank=False)
    fk_health_region = models.ForeignKey(
        HealthRegion,
        on_delete=models.CASCADE
    )

    class Meta:
        app_label = 'api'
        db_table = 'weather_station'


class Disease(models.Model):
    code = models.PositiveSmallIntegerField(blank=False)
    name = models.CharField(max_length=150, blank=False)

    # Will need to implement based on: https://www150.statcan.gc.ca/n1/en/subjects/Health
    # Allowing to be blank as not implemented yet
    classification = models.CharField(max_length=150, blank=True)
    subclassification = models.CharField(max_length=150, blank=True)

    class Meta:
        app_label = 'api'
        db_table = 'disease'

class Vaccination(models.Model):
    vaccination_name = models.CharField(max_length=150, blank=False)
    treats_disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    efficacy_rate = models.PositiveSmallIntegerField(blank=True)
    percent_pop_vaccinated = models.PositiveSmallIntegerField(blank=True)

    class Meta:
        app_label = 'api'
        db_table = 'vaccination'
