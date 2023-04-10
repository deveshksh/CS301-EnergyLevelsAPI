from django.urls import path
from .views import EnergyDataList

urlpatterns = [
    path('energy_data/', EnergyDataList.as_view(), name='energy_data_list'),
]
