from ninja import Schema
from ninja.orm import create_schema
from api.models import *

RegionSchema = create_schema(Region, 
    fields=['name_en', 'name_fr'])

ProvinceSchema = create_schema(Province, 
    fields=['geo_code', 'alpha_code', 'name_en', 'name_fr', 'fk_region', 'disease'])

ForwardSortationAreaSchema = create_schema(ForwardSortationArea, 
    fields=['code', 'eng_name', 'fre_name', 'estimated_pop', 'fk_healthregion','fk_province', 'disease'])

WeatherStationSchema = create_schema(WeatherStation, 
    fields=['cgndb_id','hr_uid', 'fk_healthregion'])

HealthRegionSchema = create_schema(HealthRegion, 
    fields=['hr_uid', 'name_en', 'name_fr', 'website_en', 'website_fr', 'fk_province', 'disease'])

DiseaseSchema = create_schema(Disease, 
    fields=['name', 'classification', 'subclassification'])

VaccinationSchema = create_schema(Vaccination, 
    fields=['name', 'efficacy_rate', 'percent_pop_vaccinated', 'fk_disease'])

HRVaccinationSchema = create_schema(HRVaccination, 
    fields=['hr_uid', 'vaccine_coverage', 'date_reported','today_date' ,'fk_disease','fk_healthregion'])  

FluwatcherSchema = create_schema(Fluwatcher, 
    fields=['hr_uid', 'confirmed_positive', 'participants', 'weekof','fk_disease','fk_healthregion']) 

class NotFoundSchema(Schema):
    message: str