
from django.urls import path
from productos.views import *

urlpatterns = [
        path('', inicio),
        path('mesas/', mesas),
        path('buscar_mesas/',buscar_mesas),
        path('api_mesas/',api_mesas)
        
]