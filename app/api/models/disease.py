from django.db import models
from api.models import *
from .geo import *


class Disease(models.Model):
    name = models.CharField(max_length=150, blank=False)

    # Will need to implement based on: https://www150.statcan.gc.ca/n1/en/subjects/Health
    # Allowing to be blank as not implemented yet
    classification = models.CharField(max_length=150, blank=True)
    subclassification = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    name = models.CharField(max_length=150, blank=False)
    efficacy_rate = models.PositiveSmallIntegerField(blank=True)
    percent_pop_vaccinated = models.PositiveSmallIntegerField(blank=True)
    fk_disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.vaccination_name


class HRVaccination(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    vaccine_coverage = models.FloatField(blank=True, null=True)
    date_reported = models.DateField(blank=True, null=True)
    today_date = models.DateField(blank=True, null=True)
    fk_disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    fk_healthregion = models.ForeignKey(
        HealthRegion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.hr_uid


class Fluwatcher(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    confirmed_positive = models.IntegerField(blank=True, null=True)
    participants = models.PositiveIntegerField(blank=True, null=True)
    weekof = models.DateField(blank=True, null=True)
    fk_disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    fk_healthregion = models.ForeignKey(
        HealthRegion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.hr_uid
