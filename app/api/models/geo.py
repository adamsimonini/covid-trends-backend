from django.db import models
from .disease import *


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



class Region(models.Model):
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name_en


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
   

    def __str__(self):
        return self.name_en


class HealthRegion(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    pop = models.PositiveBigIntegerField(blank=False)
    website_en = models.CharField(max_length=300, blank=True)
    website_fr = models.CharField(max_length=300, blank=True)
    en_prov_vaccine_site = models.CharField(max_length=300, blank=True)
    fr_prov_vaccine_site = models.CharField(max_length=300, blank=True)
    fk_province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.hr_uid


class ForwardSortationArea(models.Model):
    code = models.CharField(max_length=3, blank=False)  # first 3 digits of a postal code
    eng_name= models.CharField(max_length=150, blank=False)
    fre_name= models.CharField(max_length=150, blank=False)  
    estimated_pop = models.IntegerField(blank=True)
    fk_healthregion = models.ForeignKey(
        HealthRegion,
        on_delete=models.CASCADE
    )   
    fk_province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE
    )
    # The below is not always true since we cannot directly correlate HR and FSA since neither is the true parent or child of another
    # Therefore, we will need to simply connect FSA and HR both to Province seperately
    # health_regions = ArrayField(models.PositiveSmallIntegerField(blank=False))  # an fsa can contain multiple health regions (i.e., 1, 2, or even 3)

 

    def __str__(self):
        return self.code


class WeatherStation(models.Model):
    cgndb_id = models.CharField (max_length=5, blank=False)
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    fk_healthregion = models.ForeignKey(
        HealthRegion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.code
