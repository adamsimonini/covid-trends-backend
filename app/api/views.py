from typing import List
from ninja import NinjaAPI
from api.models import *
from .schemas import *

# Pagination not used for now although easy to implement basic functionality
# from ninja.pagination import paginate, PageNumberPagination

api = NinjaAPI()

##############################################################################
# Country
##############################################################################
@api.get('/country/', response=List[CountrySchema], 
    tags=['Countries'], summary='Get Countries', description='Gets information on all countrys')
def get_Countries(request):
    return Country.objects.all()


@api.get('/country/{name}', response={200: CountrySchema, 404: NotFoundSchema}, 
    tags=['Countries'], summary='Get a Country', description='Gets information on one single Country')
def get_Country(request, name: str):
    try:
        data = Country.objects.get(name=name)
        return 200, data
    except Country.DoesNotExist as e:
        return 404, {'message': 'Could not find Country'}


@api.post('/country/', response={201: CountrySchema}, 
    tags=['Countries'], summary='Post a Country')
def post_Country(request, data: CountrySchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    data = Country.objects.create(**Country.dict())
    return data


@api.put('/country/{name}', response={200: CountrySchema, 404: NotFoundSchema}, 
    tags=['Countries'], summary='Update a Country')
def put_Country(request, name: str, data: CountrySchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    try:
        data = Country.objects.get(name=name)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except Country.DoesNotExist as e:
        return 404, {'message': 'Could not find Country'}


@api.delete('/country/{name}', response={200: None, 404: NotFoundSchema},
    tags=['Countries'], summary='Deletes a Country', description='Allows you to delete a Country')
def delete_Country(request, name: str, data: CountrySchema):
    try:
        data = Country.objects.get(name=name)
        data.delete()
        return 200
    except Country.DoesNotExist as e:
        return 404, {'message': 'Could not find Country'}


##############################################################################
# Region
##############################################################################
@api.get('/region/', response=List[RegionSchema], 
    tags=['Regions'], summary='Get Regions', description='Gets information on all regions')
def get_Regions(request):
    return Region.objects.all()


@api.get('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema}, 
    tags=['Regions'], summary='Get a Region', description='Gets information on one single Region')
def get_Region(request, name_en: str):
    try:
        data = Region.objects.get(name_en=name_en)
        return 200, data
    except Region.DoesNotExist as e:
        return 404, {'message': 'Could not find Region'}


@api.post('/region/', response={201: RegionSchema}, 
    tags=['Regions'], summary='Post a Region')
def post_Region(request, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    data = Region.objects.create(**Region.dict())
    return data


@api.put('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema}, 
    tags=['Regions'], summary='Update a Region')
def put_Region(request, name_en: str, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    try:
        data = Region.objects.get(name_en=name_en)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except Region.DoesNotExist as e:
        return 404, {'message': 'Could not find Region'}


@api.delete('/region/{name_en}', response={200: None, 404: NotFoundSchema},
    tags=['Regions'], summary='Deletes a Region', description='Allows you to delete a Region')
def delete_Region(request, name_en: str, data: RegionSchema):
    try:
        data = Region.objects.get(name_en=name_en)
        data.delete()
        return 200
    except Region.DoesNotExist as e:
        return 404, {'message': 'Could not find Region'}


##############################################################################
# Province
##############################################################################
@api.get('/province/', response=List[ProvinceSchema], 
    tags=['Provinces'], summary='Get Provinces', description='Gets information on all provinces')
def get_Provinces(request):
    return Province.objects.all()


@api.get('/Province/{alpha_code}', response={200: ProvinceSchema, 404: NotFoundSchema}, 
    tags=['Provinces'], summary='Get a Province', description='Gets information on one single Province')
def get_Province(request, alpha_code: str):
    try:
        data = Province.objects.get(alpha_code=alpha_code)
        return 200, data
    except Province.DoesNotExist as e:
        return 404, {'message': 'Could not find Province'}


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
    data = Province.objects.create(**Province.dict())
    return data


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
    try:
        data = Province.objects.get(alpha_code=alpha_code)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except Province.DoesNotExist as e:
        return 404, {'message': 'Could not find Province'}


@api.delete('/Province/{alpha_code}', response={200: None, 404: NotFoundSchema},
    tags=['Provinces'], summary='Deletes a Province', description='Allows you to delete a Province')
def delete_Province(request, alpha_code: str, data: ProvinceSchema):
    try:
        data = Province.objects.get(alpha_code=alpha_code)
        data.delete()
        return 200
    except Province.DoesNotExist as e:
        return 404, {'message': 'Could not find Province'}

##############################################################################
# Health Region
##############################################################################
@api.get('/health_region/', response=List[HealthRegionSchema], 
    tags=['HealthRegions'], summary='Get health regions', description='Gets information on all health regions')
def get_HealthRegions(request):
    return HealthRegion.objects.all()


@api.get('/health_region/{hr_uid}', response={200: HealthRegionSchema, 404: NotFoundSchema}, 
    tags=['HealthRegions'], summary='Get a health region', description='Gets information on one single health region')
def get_HealthRegion(request, hr_uid: int):
    try:
        data = HealthRegion.objects.get(hr_uid=hr_uid)
        return 200, data
    except HealthRegion.DoesNotExist as e:
        return 404, {'message': 'Could not find health region'}


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
    data = HealthRegion.objects.create(**HealthRegion.dict())
    return data


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
    try:
        data = HealthRegion.objects.get(hr_uid=hr_uid)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except HealthRegion.DoesNotExist as e:
        return 404, {'message': 'Could not find health region'}


@api.delete('/health_region/{hr_uid}', response={200: None, 404: NotFoundSchema},
    tags=['HealthRegions'], summary='Deletes a HealthRegion', description='Allows you to delete a health region')
def delete_HealthRegion(request, hr_uid: int, data: HealthRegionSchema):
    try:
        data = HealthRegion.objects.get(hr_uid=hr_uid)
        data.delete()
        return 200
    except HealthRegion.DoesNotExist as e:
        return 404, {'message': 'Could not find HealthRegion'}


##############################################################################
# FSA
##############################################################################
@api.get('/forward_sortation_area/', response=List[ForwardSortationAreaSchema], 
    tags=['ForwardSortationAreas'], summary='Get forward sortation areas', description='Gets information on all forward sortation areas')
def get_ForwardSortationAreas(request):
    return ForwardSortationArea.objects.all()


@api.get('/forward_sortation_area/{code}', response={200: ForwardSortationAreaSchema, 404: NotFoundSchema}, 
    tags=['ForwardSortationAreas'], summary='Get a forward sortation area', description='Gets information on one single forward sortation area')
def get_ForwardSortationArea(request, code: str):
    try:
        data = ForwardSortationArea.objects.get(code=code)
        return 200, data
    except ForwardSortationArea.DoesNotExist as e:
        return 404, {'message': 'Could not find forward sortation area'}


@api.post('/forward_sortation_area/', response={201: ForwardSortationAreaSchema}, 
    tags=['ForwardSortationAreas'], summary='Post a forward sortation area')
def post_ForwardSortationArea(request, data: ForwardSortationAreaSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_province**
    
    *other fields are optional*
    """
    data = ForwardSortationArea.objects.create(**ForwardSortationArea.dict())
    return data


@api.put('/forward_sortation_area/{code}', response={200: ForwardSortationAreaSchema, 404: NotFoundSchema}, 
    tags=['ForwardSortationAreas'], summary='Update a forward sortation area')
def put_ForwardSortationArea(request, code: str, data: ForwardSortationAreaSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_province**
    
    *other fields are optional*
    """
    try:
        data = ForwardSortationArea.objects.get(code=code)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except ForwardSortationArea.DoesNotExist as e:
        return 404, {'message': 'Could not find forward sortation area'}


@api.delete('/forward_sortation_area/{code}', response={200: None, 404: NotFoundSchema},
    tags=['ForwardSortationAreas'], summary='Deletes a forward sortation area', description='Allows you to delete a forward sortation area')
def delete_ForwardSortationArea(request, code: str, data: ForwardSortationAreaSchema):
    try:
        data = ForwardSortationArea.objects.get(code=code)
        data.delete()
        return 200
    except ForwardSortationArea.DoesNotExist as e:
        return 404, {'message': 'Could not find forward sortation area'}


##############################################################################
# Weather Station
##############################################################################
@api.get('/weather_station/', response=List[WeatherStationSchema], 
    tags=['WeatherStations'], summary='Get weather stations', description='Gets information on all weather stations')
def get_WeatherStations(request):
    return WeatherStation.objects.all()


@api.get('/weather_station/{code}', response={200: WeatherStationSchema, 404: NotFoundSchema}, 
    tags=['WeatherStations'], summary='Get a weather station', description='Gets information on one single weather station')
def get_WeatherStation(request, code: int):
    try:
        data = WeatherStation.objects.get(code=code)
        return 200, data
    except WeatherStation.DoesNotExist as e:
        return 404, {'message': 'Could not find WeatherStation'}


@api.post('/weather_station/', response={201: WeatherStationSchema}, 
    tags=['WeatherStations'], summary='Post a weather station')
def post_WeatherStation(request, data: WeatherStationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_health_region**
    
    *other fields are optional*
    """
    data = WeatherStation.objects.create(**WeatherStation.dict())
    return data


@api.put('/weather_station/{code}', response={200: WeatherStationSchema, 404: NotFoundSchema}, 
    tags=['WeatherStations'], summary='Update a weather station')
def put_WeatherStation(request, code: int, data: WeatherStationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **fk_health_region**
    
    *other fields are optional*
    """
    try:
        data = WeatherStation.objects.get(code=code)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except WeatherStation.DoesNotExist as e:
        return 404, {'message': 'Could not find weather station'}


@api.delete('/weather_station/{code}', response={200: None, 404: NotFoundSchema},
    tags=['WeatherStations'], summary='Deletes a weather station', description='Allows you to delete a weather station')
def delete_WeatherStation(request, code: int, data: WeatherStationSchema):
    try:
        data = WeatherStation.objects.get(code=code)
        data.delete()
        return 200
    except WeatherStation.DoesNotExist as e:
        return 404, {'message': 'Could not find weather station'}


##############################################################################
# Disease
##############################################################################
@api.get('/disease/', response=List[DiseaseSchema], 
    tags=['Diseases'], summary='Get Diseases', description='Gets information on all diseases')
def get_diseases(request):
    return Disease.objects.all()


@api.get('/disease/{name}', response={200: DiseaseSchema, 404: NotFoundSchema}, 
    tags=['Diseases'], summary='Get a Disease', description='Gets information on one single disease')
def get_disease(request, name: str):
    try:
        data = Disease.objects.get(name=name)
        return 200, data
    except Disease.DoesNotExist as e:
        return 404, {'message': 'Could not find disease'}


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
    data = Disease.objects.create(**disease.dict())
    return data


@api.put('/disease/{name}', response={200: DiseaseSchema, 404: NotFoundSchema}, 
    tags=['Diseases'], summary='Update a disease')
def put_disease(request, name: str, data: DiseaseSchema):
    """
    Please ensure the following fields are present and not blank:
    - **code**
    - **name**
    
    *other fields are optional*
    """
    try:
        data = Disease.objects.get(name=name)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except Disease.DoesNotExist as e:
        return 404, {'message': 'Could not find disease'}


@api.delete('/disease/{name}', response={200: None, 404: NotFoundSchema},
    tags=['Diseases'], summary='Deletes a Disease', description='Allows you to delete a disease')
def delete_disease(request, name: str, data: DiseaseSchema):
    try:
        data = Disease.objects.get(name=name)
        data.delete()
        return 200
    except Disease.DoesNotExist as e:
        return 404, {'message': 'Could not find disease'}


##############################################################################
# Vaccination
##############################################################################
@api.get('/vaccination/', response=List[VaccinationSchema], 
    tags=['Vaccinations'], summary='Get vaccinations', description='Gets information on all vaccinations')
def get_Vaccinations(request):
    return Vaccination.objects.all()


@api.get('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema}, 
    tags=['Vaccinations'], summary='Get a vaccination', description='Gets information on one single vaccination')
def get_Vaccination(request, vaccination_name: str):
    try:
        data = Vaccination.objects.get(vaccination_name=vaccination_name)
        return 200, data
    except Vaccination.DoesNotExist as e:
        return 404, {'message': 'Could not find vaccination'}


@api.post('/vaccination/', response={201: VaccinationSchema}, 
    tags=['Vaccinations'], summary='Post a vaccination')
def post_Vaccination(request, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **treats_disease**
    
    *other fields are optional*
    """
    data = Vaccination.objects.create(**Vaccination.dict())
    return data


@api.put('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema}, 
    tags=['Vaccinations'], summary='Update a vaccination')
def put_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **treats_disease**
    
    *other fields are optional*
    """
    try:
        data = Vaccination.objects.get(vaccination_name=vaccination_name)
        for attribute, value in data.dict().items():
            setattr(data, attribute, value)
        data.save()
        return 200, data
    except Vaccination.DoesNotExist as e:
        return 404, {'message': 'Could not find vaccination'}


@api.delete('/vaccination/{vaccination_name}', response={200: None, 404: NotFoundSchema},
    tags=['Vaccinations'], summary='Deletes a vaccination', description='Allows you to delete a vaccination')
def delete_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    try:
        data = Vaccination.objects.get(vaccination_name=vaccination_name)
        data.delete()
        return 200
    except Vaccination.DoesNotExist as e:
        return 404, {'message': 'Could not find vaccination'}
