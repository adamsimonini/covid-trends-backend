from django.db import models


class Disease(models.Model):
    code = models.PositiveSmallIntegerField(blank=False)
    name = models.CharField(max_length=150, blank=False)

    # Will need to implement based on: https://www150.statcan.gc.ca/n1/en/subjects/Health
    # Allowing to be blank as not implemented yet
    classification = models.CharField(max_length=150, blank=True)
    subclassification = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    vaccination_name = models.CharField(max_length=150, blank=False)
    treats_disease = models.ForeignKey(
        Disease,
        on_delete=models.CASCADE
    )
    efficacy_rate = models.PositiveSmallIntegerField(blank=True)
    percent_pop_vaccinated = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.vaccination_name
