"""public_health_trends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from api.views import api
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('sql_testing/<int:hr_uid>', views.sql_testing, name="sql_testing"),
    path('__debug__/', include('debug_toolbar.urls'))  # turn off for production
]

# note, the debug toolbar works off of HTML pages, so it will not show when the URL only provides a JSON response
