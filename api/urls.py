from django.urls import path
from django.conf.urls import url
from rest_framework import routers
from api import api_views

urlpatterns = [
    url('salaries/$', api_views.SalariesAPIView.as_view(), name='salaries')
]