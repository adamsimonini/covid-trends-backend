from django.db import models

# ORM docs: https://docs.djangoproject.com/en/4.0/topics/db/models/
# fields reference: https://docs.djangoproject.com/en/4.0/ref/models/fields/#model-field-types


class Province(models.Model):
    province_code = models.PositiveSmallIntegerField(blank=False)
    full_name = models.CharField(max_length=150, blank=False)
    alpha_code = models.PositiveSmallIntegerField(blank=False)
    fk_region_id = models.PositiveSmallIntegerField(blank=False)


class Health_Region(models.Model):
    hr_uid = models.PositiveSmallIntegerField(blank=False)
    fk_province_code = models.PositiveSmallIntegerField(blank=False)
    name_en = models.CharField(max_length=150, blank=False)
    name_fr = models.CharField(max_length=150, blank=False)
    website_en = models.CharField(max_length=300, blank=False)
    website_fr = models.CharField(max_length=300, blank=False)

    # class Meta:
    #     app_label = 'api'

    # class Meta:
    #     app_label = 'derka'
