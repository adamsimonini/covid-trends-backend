from this import d
from typing import List
from ninja import NinjaAPI
from api.models import *
from .schemas import *
from .functions.CRUD import *

# Pagination not used for now although easy to implement basic functionality
# from ninja.pagination import paginate, PageNumberPagination

api = NinjaAPI()

##############################################################################
# Country
##############################################################################
@api.get('/country/', response=List[CountrySchema], 
    tags=['Countries'], summary='Get Countries', description='Gets information on all countrys')
def get_Countries(request):
    return APIFunctions(Country, CountrySchema).get_all()


@api.get('/country/{name}', response={200: CountrySchema, 404: NotFoundSchema}, 
    tags=['Countries'], summary='Get a Country', description='Gets information on one single Country')
def get_Country(request, name: str):
    return APIFunctions(Country, CountrySchema, search_input=name).get_one()


@api.post('/country/', response={201: CountrySchema}, 
    tags=['Countries'], summary='Post a Country')
def post_Country(request, data: CountrySchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Country, CountrySchema).post(data)


@api.put('/country/{name}', response={200: CountrySchema, 404: NotFoundSchema}, 
    tags=['Countries'], summary='Update a Country')
def put_Country(request, name: str, data: CountrySchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Country, CountrySchema, search_input=name).put(data)


@api.delete('/country/{name}', response={200: None, 404: NotFoundSchema},
    tags=['Countries'], summary='Deletes a Country', description='Allows you to delete a Country')
def delete_Country(request, name: str, data: CountrySchema):
    return APIFunctions(Country, CountrySchema, search_input=name).delete(data)


##############################################################################
# Region
##############################################################################
@api.get('/region/', response=List[RegionSchema], 
    tags=['Regions'], summary='Get Regions', description='Gets information on all regions')
def get_Regions(request):
    return APIFunctions(Region, RegionSchema).get_all()


@api.get('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema}, 
    tags=['Regions'], summary='Get a Region', description='Gets information on one single Region')
def get_Region(request, name_en: str):
    return APIFunctions(Region, RegionSchema, search_input=name_en).get_one()


@api.post('/region/', response={201: RegionSchema}, 
    tags=['Regions'], summary='Post a Region')
def post_Region(request, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Region, RegionSchema).post(data)


@api.put('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema}, 
    tags=['Regions'], summary='Update a Region')
def put_Region(request, name_en: str, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Region, RegionSchema, search_input=name_en).put(data)


@api.delete('/region/{name_en}', response={200: None, 404: NotFoundSchema},
    tags=['Regions'], summary='Deletes a Region', description='Allows you to delete a Region')
def delete_Region(request, name_en: str, data: RegionSchema):
    return APIFunctions(Region, RegionSchema, search_input=name_en).delete(data)


##############################################################################
# Province
##############################################################################
@api.get('/province/', response=List[ProvinceSchema], 
    tags=['Provinces'], summary='Get Provinces', description='Gets information on all provinces')
def get_Provinces(request):
    return APIFunctions(Province, ProvinceSchema).get_all()


@api.get('/Province/{alpha_code}', response={200: ProvinceSchema, 404: NotFoundSchema}, 
    tags=['Provinces'], summary='Get a Province', description='Gets information on one single Province')
def get_Province(request, alpha_code: str):
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).get_one()


@api.post('/Province/', response={201: ProvinceSchema}, 
    tags=['Provinces'], summary='Post a Province')
def post_Province(request, data: ProvinceSchema):
    """
    Please ensure the following fields are present and not blank:
    - **geo_code**
    - **alpha_code**
    - **name_en**
    - **name_fr**
    - **fk_region**
    
    *other fields are optional*
    """
    return APIFunctions(Province, ProvinceSchema).post(data)


@api.put('/Province/{alpha_code}', response={200: ProvinceSchema, 404: NotFoundSchema}, 
    tags=['Provinces'], summary='Update a Province')
def put_Province(request, alpha_code: str, data: ProvinceSchema):
    """
    Please ensure the following fields are present and not blank:
    - **geo_code**
    - **alpha_code**
    - **name_en**
    - **name_fr**
    - **fk_region**
    
    *other fields are optional*
    """
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).put(data)


@api.delete('/Province/{alpha_code}', response={200: None, 404: NotFoundSchema},
    tags=['Provinces'], summary='Deletes a Province', description='Allows you to delete a Province')
def delete_Province(request, alpha_code: str, data: ProvinceSchema):
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).delete(data)

##############################################################################
# Health Region
##############################################################################
@api.get('/health_region/', response=List[HealthRegionSchema], 
    tags=['HealthRegions'], summary='Get health regions', description='Gets information on all health regions')
def get_HealthRegions(request):
    return APIFunctions(HealthRegion, HealthRegionSchema).get_all()


@api.get('/health_region/{hr_uid}', response={200: HealthRegionSchema, 404: NotFoundSchema}, 
    tags=['HealthRegions'], summary='Get a health region', description='Gets information on one single health region')
def get_HealthRegion(request, hr_uid: int):
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).get_one()


@api.post('/health_region/', response={201: HealthRegionSchema}, 
    tags=['HealthRegions'], summary='Post a health region')
def post_HealthRegion(request, data: HealthRegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **name_en**
    - **name_fr**
    - **website_en**
    - **website_fr**
    - **fk_province**
    
    *other fields are optional*
    """
    return APIFunctions(HealthRegion, HealthRegionSchema).post(data)


@api.put('/health_region/{hr_uid}', response={200: HealthRegionSchema, 404: NotFoundSchema}, 
    tags=['HealthRegions'], summary='Update a health region')
def put_HealthRegion(request, hr_uid: int, data: HealthRegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **name_en**
    - **name_fr**
    - **website_en**
    - **website_fr**
    - **fk_province**
    
    *other fields are optional*
    """
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).put(data)


@api.delete('/health_region/{hr_uid}', response={200: None, 404: NotFoundSchema},
    tags=['HealthRegions'], summary='Deletes a HealthRegion', description='Allows you to delete a health region')
def delete_HealthRegion(request, hr_uid: int, data: HealthRegionSchema):
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).delete(data)


##############################################################################
# FSA
##############################################################################
@api.get('/forward_sortation_area/', response=List[ForwardSortationAreaSchema], 
    tags=['ForwardSortationAreas'], summary='Get forward sortation areas', description='Gets information on all forward sortation areas')
def get_ForwardSortationAreas(request):
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema).get_all()


@api.get('/forward_sortation_area/{code}', response={200: ForwardSortationAreaSchema, 404: NotFoundSchema}, 
    tags=['ForwardSortationAreas'], summary='Get a forward sortation area', description='Gets information on one single forward sortation area')
def get_ForwardSortationArea(request, code: str):
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema, search_input=code).get_one()


@api.post('/forward_sortation_area/', response={201: ForwardSortationAreaSchema}, 
    tags=['ForwardSortationAreas'], summary='Post a forward sortation area')
def post_ForwardSortationArea(request, data: ForwardSortationAreaSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_province**
    
    *other fields are optional*
    """
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema).post(data)


@api.put('/forward_sortation_area/{code}', response={200: ForwardSortationAreaSchema, 404: NotFoundSchema}, 
    tags=['ForwardSortationAreas'], summary='Update a forward sortation area')
def put_ForwardSortationArea(request, code: str, data: ForwardSortationAreaSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_province**
    
    *other fields are optional*
    """
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema, search_input=code).put(data)


@api.delete('/forward_sortation_area/{code}', response={200: None, 404: NotFoundSchema},
    tags=['ForwardSortationAreas'], summary='Deletes a forward sortation area', description='Allows you to delete a forward sortation area')
def delete_ForwardSortationArea(request, code: str, data: ForwardSortationAreaSchema):
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema, search_input=code).delete(data)


##############################################################################
# Weather Station
##############################################################################
@api.get('/weather_station/', response=List[WeatherStationSchema], 
    tags=['WeatherStations'], summary='Get weather stations', description='Gets information on all weather stations')
def get_WeatherStations(request):
    return APIFunctions(WeatherStation, WeatherStationSchema).get_all()


@api.get('/weather_station/{code}', response={200: WeatherStationSchema, 404: NotFoundSchema}, 
    tags=['WeatherStations'], summary='Get a weather station', description='Gets information on one single weather station')
def get_WeatherStation(request, code: int):
    return APIFunctions(WeatherStation, WeatherStationSchema, search_input=code).get_one()


@api.post('/weather_station/', response={201: WeatherStationSchema}, 
    tags=['WeatherStations'], summary='Post a weather station')
def post_WeatherStation(request, data: WeatherStationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_health_region**
    
    *other fields are optional*
    """
    return APIFunctions(WeatherStation, WeatherStationSchema).post(data)


@api.put('/weather_station/{code}', response={200: WeatherStationSchema, 404: NotFoundSchema}, 
    tags=['WeatherStations'], summary='Update a weather station')
def put_WeatherStation(request, code: int, data: WeatherStationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_health_region**
    
    *other fields are optional*
    """
    return APIFunctions(WeatherStation, WeatherStationSchema, search_input=code).put(data)


@api.delete('/weather_station/{code}', response={200: None, 404: NotFoundSchema},
    tags=['WeatherStations'], summary='Deletes a weather station', description='Allows you to delete a weather station')
def delete_WeatherStation(request, code: int, data: WeatherStationSchema):
    return APIFunctions(WeatherStation, WeatherStationSchema, search_input=code).delete(data)


##############################################################################
# Disease
##############################################################################
@api.get('/disease/', response=List[DiseaseSchema], 
    tags=['Diseases'], summary='Get Diseases', description='Gets information on all diseases')
def get_diseases(request):
    return APIFunctions(Disease, DiseaseSchema).get_all()


@api.get('/disease/{name}', response={200: DiseaseSchema, 404: NotFoundSchema}, 
    tags=['Diseases'], summary='Get a Disease', description='Gets information on one single disease')
def get_disease(request, name: str):
    return APIFunctions(Disease, DiseaseSchema, search_input=name).get_one()


@api.post('/disease/', response={201: DiseaseSchema}, 
    tags=['Diseases'], summary='Post a Disease')
def post_disease(request, data: DiseaseSchema):
    """
    Add information for a disease

    To add a disease please provide:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Disease, DiseaseSchema).post(data)


@api.put('/disease/{name}', response={200: DiseaseSchema, 404: NotFoundSchema}, 
    tags=['Diseases'], summary='Update a disease')
def put_disease(request, name: str, data: DiseaseSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    return APIFunctions(Disease, DiseaseSchema, search_input=name).put(data)


@api.delete('/disease/{name}', response={200: None, 404: NotFoundSchema},
    tags=['Diseases'], summary='Deletes a Disease', description='Allows you to delete a disease')
def delete_disease(request, name: str, data: DiseaseSchema):
    return APIFunctions(Disease, DiseaseSchema, search_input=name).delete(data)


##############################################################################
# Vaccination
##############################################################################
@api.get('/vaccination/', response=List[VaccinationSchema], 
    tags=['Vaccinations'], summary='Get vaccinations', description='Gets information on all vaccinations')
def get_Vaccinations(request):
    return APIFunctions(Vaccination, VaccinationSchema).get_all()


@api.get('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema}, 
    tags=['Vaccinations'], summary='Get a vaccination', description='Gets information on one single vaccination')
def get_Vaccination(request, vaccination_name: str):
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).get_one()


@api.post('/vaccination/', response={201: VaccinationSchema}, 
    tags=['Vaccinations'], summary='Post a vaccination')
def post_Vaccination(request, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **treats_disease**
    
    *other fields are optional*
    """
    return APIFunctions(Vaccination, VaccinationSchema).post(data)


@api.put('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema}, 
    tags=['Vaccinations'], summary='Update a vaccination')
def put_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **treats_disease**
    
    *other fields are optional*
    """
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).put(data)


@api.delete('/vaccination/{vaccination_name}', response={200: None, 404: NotFoundSchema},
    tags=['Vaccinations'], summary='Deletes a vaccination', description='Allows you to delete a vaccination')
def delete_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).delete(data)
