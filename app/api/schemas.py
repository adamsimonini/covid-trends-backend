from ninja import Schema
from ninja.orm import create_schema
from api.models import *

CountrySchema = create_schema(Country, 
    fields=['code', 'name'])

RegionSchema = create_schema(Region, 
    fields=['name_en', 'name_fr'])

ProvinceSchema = create_schema(Province, 
    fields=['geo_code', 'alpha_code', 'name_en', 'name_fr', 'fk_region', 'disease'])

ForwardSortationAreaSchema = create_schema(ForwardSortationArea, 
    fields=['code', 'fk_province', 'disease'])

WeatherStationSchema = create_schema(WeatherStation, 
    fields=['code', 'fk_health_region'])

HealthRegionSchema = create_schema(HealthRegion, 
    fields=['hr_uid', 'name_en', 'name_fr', 'website_en', 'website_fr', 'fk_province', 'disease'])

DiseaseSchema = create_schema(Disease, 
    fields=['code', 'name', 'classification', 'subclassification'])

VaccinationSchema = create_schema(Vaccination, 
    fields=['vaccination_name', 'efficacy_rate', 'percent_pop_vaccinated', 'fk_disease'])

class NotFoundSchema(Schema):
    message: str