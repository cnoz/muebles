from django.urls import path

from tienda.views import tienda


urlpatterns = [
   
   
    path('tienda/', tienda),
   
    
]