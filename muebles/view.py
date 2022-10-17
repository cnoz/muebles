from django.http import HttpResponse
from django.template import loader
#from productos.models import *



def home(request):
    planilla = loader.get_template('home2.html')
    documento =planilla.render()
    return HttpResponse(documento)


