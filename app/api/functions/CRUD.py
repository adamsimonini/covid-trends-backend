from statistics import mode
from telnetlib import STATUS
from typing import List
from api.models import *

from ninja import Schema
from ..schemas import *

class APIFunctions():
    #TODO : fix error message to reflect erorr dedicated to each table. 
    ERROR_REPLY = {'message': 'info does not exist'}

    # Initializes the class and defines the type hints
    def __init__(self, model: models.Model, schema: Schema, search_input = None):
        self.model = model
        self.schema = schema
        self.search_input = search_input

    # Generates the info variable used in searches
    def get_search_variable(self):
        info = []

     
        if self.model == disease:
            info = self.model.objects.get(name=self.search_input)
        elif self.model == Region:
            info = self.model.objects.get(name_en=self.search_input)
        elif self.model == Province:
            info = self.model.objects.get(alpha_code=self.search_input)
        elif self.model == HealthRegion:
            info = self.model.objects.get(hr_uid=self.search_input)
        elif self.model == ForwardSortationArea:
            info = self.model.objects.get(code=self.search_input)
        elif self.model == WeatherStation:
            info = self.model.objects.get(code=self.search_input)
        elif self.model == Vaccination:
            info = self.model.objects.get(vaccination_name=self.search_input)
        elif self.model == HRVaccination:
            info = self.model.objects.get(hr_uid=self.search_input)
        elif self.model == Fluwatcher:
            info = self.model.objects.get(hr_uid=self.search_input)
        
        # Error handling
        if info != []:
            return info
        else:
            raise self.model.DoesNotExist

    # GET ALL
    def get_all(self):
        return self.model.objects.all()

    # GET ONE
    def get_one(self):
        try:
            info = self.get_search_variable()
            return 200, info
        except:
            return 404, self.ERROR_REPLY

    # POST
    def post(self, data: Schema):
        self.schema = self.model.objects.create(**data.dict())
        return self.schema

    # PUT
    def put(self, data: Schema):
        try:
            info = self.get_search_variable()
            for attribute, value in data.dict().items():
                setattr(info, attribute, value)
            info.save()
            return 200, info
        except:
            return 404, self.ERROR_REPLY

    # DELETE
    def delete(self, data: Schema):
        try:
            info = self.get_search_variable()
            info.delete()
            return 200
        except self.model.DoesNotExist as e:
            return 404, self.ERROR_REPLY