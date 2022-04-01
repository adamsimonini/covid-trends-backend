"""
----------------------------------------------------------------
docker compose up -d
make migrations/migrate/load geo_fixtures
cd app/
pytest
----------------------------------------------------------------
"""

from django import urls
from django.contrib.auth import get_user_model
import pytest 
import api.urls


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass



@pytest.mark.parametrize('param', [
    ('index'),
    ('region'),
    ('country'),
    ('health_region'),
    ('disease'),
    ('weatherstation'),
    ('province'),
    ('vaccination'),
   
])


def test_render_views(client, param):    
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200



  
  