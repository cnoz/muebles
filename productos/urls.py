
from django.urls import path
from productos.views import *

urlpatterns = [
        path('', inicio),
        path('mesas/', mesas),
        path('buscar_mesas/',buscar_mesas),
        path('api_mesas/',api_mesas),
        path('sillas/', sillas),
        path('buscar_sillas/',buscar_sillas),
        path('api_sillas/', api_sillas),
        path('sofa/', sofa),
        path('buscar_sofa/',buscar_sofa),
        path('api_sofa/', api_sofa),
        path('usuario/', usuario),
        path('buscar_usuario/',buscar_usuario),
        path('api_usuario/', api_usuario)
]