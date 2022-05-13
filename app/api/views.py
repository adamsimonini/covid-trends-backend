from this import d
from typing import List
from ninja import NinjaAPI
from api.models import *
from .schemas import *
from .functions.CRUD import *
from django.http import JsonResponse  # dev only
from django.shortcuts import render  # dev only
from django.template import loader  # dev only

# TODO : Create more details on errors
# TODO : Find out why the first record is not showing
# TODO : Make message more direct of each end point
# TODO : Syntax is consistent. Underscore for spaces, lower case.....
# TODO : Post and Put do not work. look into permissions?

# Pagination not used for now although easy to implement basic functionality
# from ninja.pagination import paginate, PageNumberPagination

api = NinjaAPI()

# >>> for p in Person.objects.raw('SELECT * FROM myapp_person'):
# ...     print(p)
# John Smith
# Jane Jones

# DJANGO ORM "select_related": https://www.youtube.com/watch?v=TzgZBg7oXNA

# making queries: https://docs.djangoproject.com/en/4.0/topics/db/queries/
# query sets: https://docs.djangoproject.com/en/4.0/ref/models/querysets/


@api.get('/health_region_full/{hr_uid}', tags=['healthregion'], summary='Get all healthregion data for COVID-10',
         description='Returns the province, health region, fluwatchers, and hrVaccination data')
def single_health_region_COVID_19(request, hr_uid: int):

    data = {}

    # create a QuerySet targetting the appropriate health region
    healthRegionQS = HealthRegion.objects.get(hr_uid=hr_uid)

    # executive various QuerySets to get the health region, fluwatcher, and hr_vax data for that health region
    healthRegionDict = HealthRegion.objects.values("hr_uid", "name_en", "name_fr").get(hr_uid=hr_uid)
    fluwatcherDict = healthRegionQS.fluwatcher_set.values("confirmed_positive", "participants", "weekof").get()
    hrVaccinationDict = healthRegionQS.hrvaccination_set.values("vaccine_coverage", "date_reported", "today_date").get()

    # create a new QuerySet for province and execute it, to get the appropriate province back
    provinceDict = Province.objects.filter(healthregion__hr_uid=hr_uid).values().get()

    # place all returned diectionries from querying the database into the data dictionry
    data["health_region"] = healthRegionDict
    data["fluwatcher"] = fluwatcherDict
    data["hr_vaccination"] = hrVaccinationDict
    data["province"] = provinceDict

    # return data dictionary as the JSON response
    return data


def sql_testing(request, hr_uid: int):
    # qs3 = list(HealthRegion.objects.select_related("fk_province").all())
    # https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward

    # Values(): https://docs.djangoproject.com/en/4.0/ref/models/querysets/#values
    # Get(): https://docs.djangoproject.com/en/4.0/topics/db/queries/#retrieving-a-single-object-with-get
    healthRegionQS = HealthRegion.objects.get(hr_uid=hr_uid)
    healthRegionDict = HealthRegion.objects.values("hr_uid", "name_en", "name_fr").get(hr_uid=hr_uid)
    # get() is empty because the QS identifies only one record, else get would need parameters like above
    fluwatcherDict = healthRegionQS.fluwatcher_set.values("confirmed_positive", "participants", "weekof").get()
    hrVaccinationDict = healthRegionQS.hrvaccination_set.values("vaccine_coverage", "date_reported", "today_date").get()

    print(healthRegionDict)
    print(fluwatcherDict)
    print(hrVaccinationDict)

    # print(hr_id_2.name_en)
    # print(hr_id_2.fk_province)
    # for a querySet (HealthRegion.objects.get(id=2)), if it's related to given model (Fluwatcher), return the records for that model matching the querySet
    # fluwatcher_for_hr_3 = list(healthRegionQS.fluwatcher_set.all())  # returns fluwatcher data for the fluwatcher record with fk_healthregion_id of 3
    # hr_vaccination_for_hr_3 = list(healthRegionQS.hrvaccination_set.all())  # returns hrvaccination data for the hrvaccination record with fk_healthregion_id of 3

    # now that we have the health region, we can get the province joined to that health region
    # prov_for_hr = healthRegionQS.fk_province
    # print(prov_for_hr)

    # fluwatcherHR = HealthRegion.objects.select_related("fk_healthregion")
    # vaccineHR = HRVaccination.objects.select_related("fk_healthregion")
    q1 = Fluwatcher.objects.values('id', 'hr_uid', 'confirmed_positive', 'participants', 'weekof', 'fk_disease_id', 'fk_healthregion_id').all()
    context = {
        "data": healthRegionQS
    }
    # q3 = querySet.filter(hr_uid=1012)
    # q4 = querySet.filter(hr_uid=1013)
    return render(request, "sql_testing.html", context)
    # qs2 = list(Fluwatcher.objects.all())


@api.get('/hr_province_one/',
         tags=['hr-prov-1'], summary='Get hr-prov',
         description='Health regions are defined by provincial ministries of health. This Function gets information on all health regions')
def get_hr_province_one(request):
    # data = HealthRegion.objects.select_related('fk_province').all().values_list("name_en", "pop", "en_prov_vaccine_site", "forwardsortationarea, weatherstation, fluwatcher")
    # data = HealthRegion.objects.select_related("fk_province").get(id=1).values_list("name_en", "pop", "fk_province")
    # for hr in data:
    #     print(hr)
    # print(hr)
    hr_plus_prov = HealthRegion.objects.select_related("fk_province").all()

    for hr in hr_plus_prov:
        print(hr.name_en, hr.fk_province.name_en, hr.fk_province.alpha_code)

    hr_plus_prov_list = list(hr_plus_prov.values())

    return JsonResponse({'data': hr_plus_prov_list})

    # return JsonResponse({"test": "hello"})
    # return JsonResponse({"response": list(data)})


@api.get('/hr_province_two/{disease}/{hr_id}',
         tags=['hr-prov-2'], summary='Get info on a specific dieases and hr',
         description='Health regions are defined by provincial ministries of health. This Function gets information on all health regions')
def get_hr_province_two(request, disease: str, hr_id):
    hr_querty_set = HealthRegion.objects.select_related("vaccine_coverage", "confirmed_positive", "participants").filter(hr_uid=hr_id)
    for hr in hr_querty_set:
        print(hr.name_en, hr.vaccine_coverage)
    return "hello"
    ##############################################################################
    # Region
    ##############################################################################


@api.get('/region/', response=List[RegionSchema],
         tags=['Regions'], summary='Get Regions',
         description='Regions are representations of the Canadian geographic regions of Canada. This will get information on all regions.')
def get_Regions(request):
    return APIFunctions(Region, RegionSchema).get_all()


@api.get('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema},
         tags=['Regions'], summary='Get a Region',
         description='Regions are representations of the Canadian geographic regions of Canada. This will get information on a region. Records can be accessed by using the English name. For example "Atlantic" or "territories"')
def get_Region(request, name_en: str):
    return APIFunctions(Region, RegionSchema, search_input=name_en).get_one()


@api.post('/region/', response={201: RegionSchema},
          tags=['Regions'], summary='Post a Region')
def post_Region(request, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **name_en - String**
    - **name_fr - String**

    *other fields are optional*
    """
    return APIFunctions(Region, RegionSchema).post(data)


@api.put('/region/{name_en}', response={200: RegionSchema, 404: NotFoundSchema},
         tags=['Regions'], summary='Update a Region')
def put_Region(request, name_en: str, data: RegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **name_en - String**
    - **name_fr - String**

    *other fields are optional*
    """
    return APIFunctions(Region, RegionSchema, search_input=name_en).put(data)


@api.delete('/region/{name_en}', response={200: None, 404: NotFoundSchema},
            tags=['Regions'], summary='Deletes a Region',
            description='Allows you to delete a Region')
def delete_Region(request, name_en: str, data: RegionSchema):
    return APIFunctions(Region, RegionSchema, search_input=name_en).delete(data)


##############################################################################
# Province
##############################################################################
@api.get('/province/', response=List[ProvinceSchema],
         tags=['Provinces'], summary='Get Provinces',
         description='Gets information on all provinces')
def get_Provinces(request):
    return APIFunctions(Province, ProvinceSchema).get_all()


@api.get('/province/{alpha_code}', response={200: ProvinceSchema, 404: NotFoundSchema},
         tags=['Provinces'], summary='Get a Province',
         description='Gets information on a single province or territory. We expect an alpha_code to be provided such as "AB" or "QC". \
    Alpha_code must be capitalized. For example, the province of Ontario = "ON"')
def get_Province(request, alpha_code: str):
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).get_one()


@api.post('/province/', response={201: ProvinceSchema},
          tags=['Provinces'], summary='Post a Province')
def post_Province(request, data: ProvinceSchema):
    """
    Please ensure the following fields are present and not blank:
    - **geo_code - String**
    - **alpha_code - String**
    - **name_en - String**
    - **name_fr - String**
    - **fk_region - Integer**

    *other fields are optional*
    """
    return APIFunctions(Province, ProvinceSchema).post(data)


@api.put('/province/{alpha_code}', response={200: ProvinceSchema, 404: NotFoundSchema},
         tags=['Provinces'], summary='Update a Province')
def put_Province(request, alpha_code: str, data: ProvinceSchema):
    """
    Please ensure the following fields are present and not blank:
    - **geo_code - String**
    - **alpha_code - String**
    - **name_en - String**
    - **name_fr - String**
    - **fk_region - Integer**

    *other fields are optional*
    """
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).put(data)


@api.delete('/province/{alpha_code}', response={200: None, 404: NotFoundSchema},
            tags=['Provinces'], summary='Deletes a Province',
            description='Allows you to delete a Province')
def delete_Province(request, alpha_code: str, data: ProvinceSchema):
    return APIFunctions(Province, ProvinceSchema, search_input=alpha_code).delete(data)

##############################################################################
# Health Region
##############################################################################


@api.get('/health_region/', response=List[HealthRegionSchema],
         tags=['HealthRegions'], summary='Get health regions',
         description='Health regions are defined by provincial ministries of health. This Function gets information on all health regions')
def get_HealthRegions(request):
    return APIFunctions(HealthRegion, HealthRegionSchema).get_all()


@api.get('/health_region/{hr_uid}', response={200: HealthRegionSchema, 404: NotFoundSchema},
         tags=['HealthRegions'], summary='Get a health region',
         description='Gets information on a single health region. We expect a Health Region Unit Identifying (hr_uid) code such as "2402" or "591". The hr_uid must be an interger. For example  the Montreal Health Region = "2406" ')
def get_HealthRegion(request, hr_uid: int):
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).get_one()


@api.post('/health_region/', response={201: HealthRegionSchema},
          tags=['HealthRegions'], summary='Post a health region')
def post_HealthRegion(request, data: HealthRegionSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid - Integer**
    - **name_en - String**
    - **name_fr - String**
    - **website_en - String**
    - **website_fr - String**
    - **fk_province - Integer**

    *other fields are optional*
    """
    return APIFunctions(HealthRegion, HealthRegionSchema).post(data)


@api.put('/health_region/{hr_uid}', response={200: HealthRegionSchema, 404: NotFoundSchema},
         tags=['HealthRegions'], summary='Update a health region')
def put_HealthRegion(request, hr_uid: int, data: HealthRegionSchema):
    """
    Please ensure the following fields are present and not blank:
   - **hr_uid - Integer**
    - **name_en - String**
    - **name_fr - String**
    - **website_en - String**
    - **website_fr - String**
    - **fk_province - Integer**

    *other fields are optional*
    """
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).put(data)


@api.delete('/health_region/{hr_uid}', response={200: None, 404: NotFoundSchema},
            tags=['HealthRegions'], summary='Deletes a HealthRegion',
            description='Allows you to delete a health region')
def delete_HealthRegion(request, hr_uid: int, data: HealthRegionSchema):
    return APIFunctions(HealthRegion, HealthRegionSchema, search_input=hr_uid).delete(data)


##############################################################################
# FSA
##############################################################################
@api.get('/forward_sortation_area/', response=List[ForwardSortationAreaSchema],
         tags=['ForwardSortationAreas'], summary='Get forward sortation areas',
         description='Gets information on all forward sortation areas')
def get_ForwardSortationAreas(request):
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema).get_all()


@api.get('/forward_sortation_area/{code}', response={200: ForwardSortationAreaSchema, 404: NotFoundSchema},
         tags=['ForwardSortationAreas'], summary='Get a forward sortation area',
         description='Gets information on one single forward sortation area')
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
            tags=['ForwardSortationAreas'], summary='Deletes a forward sortation area',
            description='Allows you to delete a forward sortation area')
def delete_ForwardSortationArea(request, code: str, data: ForwardSortationAreaSchema):
    return APIFunctions(ForwardSortationArea, ForwardSortationAreaSchema, search_input=code).delete(data)


##############################################################################
# Weather Station
##############################################################################
@api.get('/weather_station/', response=List[WeatherStationSchema],
         tags=['WeatherStations'], summary='Get weather stations',
         description='Gets information on all weather stations')
def get_WeatherStations(request):
    return APIFunctions(WeatherStation, WeatherStationSchema).get_all()


@api.get('/weather_station/{code}', response={200: WeatherStationSchema, 404: NotFoundSchema},
         tags=['WeatherStations'], summary='Get a weather station',
         description='Gets information on one single weather station')
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
            tags=['WeatherStations'], summary='Deletes a weather station',
            description='Allows you to delete a weather station')
def delete_WeatherStation(request, code: int, data: WeatherStationSchema):
    return APIFunctions(WeatherStation, WeatherStationSchema, search_input=code).delete(data)


##############################################################################
# Disease
##############################################################################
@api.get('/disease/', response=List[DiseaseSchema],
         tags=['Diseases'], summary='Get Diseases',
         description='Gets information on all diseases')
def get_diseases(request):
    return APIFunctions(Disease, DiseaseSchema).get_all()


@api.get('/disease/{name}', response={200: DiseaseSchema, 404: NotFoundSchema},
         tags=['Diseases'], summary='Get a Disease',
         description='Gets information on one single disease')
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
            tags=['Diseases'], summary='Deletes a Disease',
            description='Allows you to delete a disease')
def delete_disease(request, name: str, data: DiseaseSchema):
    return APIFunctions(Disease, DiseaseSchema, search_input=name).delete(data)


##############################################################################
# Vaccination
##############################################################################
@api.get('/vaccination/', response=List[VaccinationSchema],
         tags=['Vaccinations'], summary='Get vaccinations',
         description='Gets information on all vaccinations')
def get_Vaccinations(request):
    return APIFunctions(Vaccination, VaccinationSchema).get_all()


@api.get('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema},
         tags=['Vaccinations'], summary='Get a vaccination',
         description='Gets information on one single vaccination')
def get_Vaccination(request, vaccination_name: str):
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).get_one()


@api.post('/vaccination/', response={201: VaccinationSchema},
          tags=['Vaccinations'], summary='Post a vaccination')
def post_Vaccination(request, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(Vaccination, VaccinationSchema).post(data)


@api.put('/vaccination/{vaccination_name}', response={200: VaccinationSchema, 404: NotFoundSchema},
         tags=['Vaccinations'], summary='Update a vaccination')
def put_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **vaccination_name**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).put(data)


@api.delete('/vaccination/{vaccination_name}', response={200: None, 404: NotFoundSchema},
            tags=['Vaccinations'], summary='Deletes a vaccination',
            description='Allows you to delete a vaccination')
def delete_Vaccination(request, vaccination_name: str, data: VaccinationSchema):
    return APIFunctions(Vaccination, VaccinationSchema, search_input=vaccination_name).delete(data)


##############################################################################
# HRVaccination
##############################################################################
@api.get('/hr_vaccination/', response=List[HRVaccinationSchema],
         tags=['HRVaccinations'], summary='Get hrvaccinations',
         description='Gets information on all hrvaccinations')
def get_HRVaccinations(request):
    return APIFunctions(HRVaccination, HRVaccinationSchema).get_all()


@api.get('/hr_vaccination/{hr_uid}', response={200: HRVaccinationSchema, 404: NotFoundSchema},
         tags=['HRVaccinations'], summary='Get a hrvaccination',
         description='Gets information on one single hrvaccination')
def get_HRVaccination(request, hr_uid: str):
    return APIFunctions(HRVaccination, HRVaccinationSchema, search_input=hr_uid).get_one()


@api.post('/hr_vaccination/', response={201: HRVaccinationSchema},
          tags=['HRVaccinations'], summary='Post a hrvaccination')
def post_HRVaccination(request, data: HRVaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(HRVaccination, HRVaccinationSchema).post(data)


@api.put('/hr_vaccination/{hr_uid}', response={200: HRVaccinationSchema, 404: NotFoundSchema},
         tags=['HRVaccinations'], summary='Update a hrvaccination')
def put_HRVaccination(request, hr_uid: str, data: HRVaccinationSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(HRVaccination, HRVaccinationSchema, search_input=hr_uid).put(data)


@api.delete('/hr_vaccination/{hr_uid}', response={200: None, 404: NotFoundSchema},
            tags=['HRVaccinations'], summary='Deletes a hrvaccination',
            description='Allows you to delete a hrvaccination')
def delete_HRVaccination(request, hr_uid: str, data: HRVaccinationSchema):
    return APIFunctions(HRVaccination, HRVaccinationSchema, search_input=hr_uid).delete(data)


##############################################################################
# Fluwatcher
##############################################################################

@api.get('/fluwatcher/', response=List[FluwatcherSchema],
         tags=['Fluwatcher'], summary='Get fluwatcher',
         description='Gets information on all fluwatcher')
def get_Fluwatchers(request):
    return APIFunctions(Fluwatcher, FluwatcherSchema).get_all()


@api.get('/fluwatcher/{hr_uid}', response={200: FluwatcherSchema, 404: NotFoundSchema},
         tags=['Fluwatcher'], summary='Get a Fluwatcher',
         description='Gets information on one single Fluwatcher')
def get_Fluwatcher(request, hr_uid: str):
    return APIFunctions(Fluwatcher, FluwatcherSchema, search_input=hr_uid).get_one()


@api.post('/fluwatcher/', response={201: FluwatcherSchema},
          tags=['Fluwatcher'], summary='Post a Fluwatcher')
def post_Fluwatcher(request, data: FluwatcherSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(Fluwatcher, FluwatcherSchema).post(data)


@api.put('/fluwatcher/{hr_uid}', response={200: FluwatcherSchema, 404: NotFoundSchema},
         tags=['Fluwatcher'], summary='Update a Fluwatcher')
def put_Fluwatcher(request, hr_uid: str, data: FluwatcherSchema):
    """
    Please ensure the following fields are present and not blank:
    - **hr_uid**
    - **fk_disease**

    *other fields are optional*
    """
    return APIFunctions(Fluwatcher, FluwatcherSchema, search_input=hr_uid).put(data)


@api.delete('/fluwatcher/{hr_uid}', response={200: None, 404: NotFoundSchema},
            tags=['Fluwatcher'], summary='Deletes a Fluwatcher', description='Allows you to delete a Fluwatcher')
def delete_Fluwatcher(request, hr_uid: str, data: FluwatcherSchema):
    return APIFunctions(Fluwatcher, FluwatcherSchema, search_input=hr_uid).delete(data)
