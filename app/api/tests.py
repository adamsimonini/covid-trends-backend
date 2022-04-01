"""
----------------------------------------------------------------
docker compose up -d
cd app/
python ./manage.py test

----------------------------------------------------------------
"""

from rest_framework.test import APITestCase

from api.models import Disease 

# def test_basic():
#     assert 1 == 1



class DiseaseCreateTestCase(APITestCase):
    def test_create_disease(self):
        initial_disease_count = Disease.objects.count()
        disease_attrs = {
            'code': '1234',
            'name': 'New Disease',
            'classification': 'New Classification', 
            'subclassification' : 'New Subclassification',        
        }
        response = self.client.post('/api/disease/new', disease_attrs)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Disease.objects.count(),
            initial_disease_count + 1,
        )


"""
----------------------------------------------------------------
DiseaseDestroyTestCase is not yet functional. 
Leave commented out at this time
----------------------------------------------------------------
"""
# class DiseaseDestroyTestCase(APITestCase):
#     def test_delete_disease(self):
#         initial_disease_count = Disease.objects.count()
#         disease_id = Disease.objects.first().id
#         self.client.delete('/api/disease/'.format(disease_id))
#         self.assertEqual(
#             Disease.objects.count(),
#             initial_disease_count - 1,
#         )
#         self.assertRaises(
#             Disease.DoesNotExist,
#             Disease.objects.get, id=disease_id,
#         )


class DiseaseListTestCase(APITestCase):
    def test_list_region(self):
        disease_count = Disease.objects.count()
        response = self.client.get('/api/disease/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], disease_count)
        self.assertEqual(len(response.data['results']), disease_count)



"""
----------------------------------------------------------------
test_an_admin_view is not yet functional.  
Leave commented out at this time
----------------------------------------------------------------
"""
# def test_an_admin_view(admin_client):
#     response = admin_client.get('/admin/')
#     assert response.status_code == 200





   