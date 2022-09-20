from django.shortcuts import render
from django.http import HttpResponse
from productos.forms import form_mesas, form_sillas, form_sillones, form_usuario
from productos.models import *

# Create your views here.


def inicio(request):
    return render(request, 'index.html')

########################################################
def mesas(request):
    if request.method == "POST":
        mesa = Mesa(nombre=request.POST['nombre'], material=request.POST['material'],tipo=request.POST['tipo'],precio=request.POST['precio'])
        mesa.save()
        return render(request, "index.html")
    return render(request, "mesas.html")

def buscar_mesas(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        mesas = Mesa.objects.filter(nombre__icontains= nombre)
        return render(request, "mesas.html", {'mesas': mesas})
    #elif request.GET['material']:
    #    material = request.GET['material']
    #    material = Mesa.objects.filter(material__icontains= material)
    #    return render(request, "mesas.html", {'material': material})
    #
    
    else:
        respuesta = "No enviaste datos"
    #return render(request, "estudiantes.html") #si no cargo datos se queda en la pag.
    return HttpResponse(respuesta)

def api_mesas(request):
    if request.method == "POST":
        formulario = form_mesas(request.POST)
        print(formulario)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            mesa = Mesa(nombre= informacion['nombre'], material= informacion['material'], tipo= informacion['tipo'], precio= informacion['precio'])
            mesa.save()
            return render(request, 'api_mesas.html')
    else:
        formulario = form_mesas()
    return render(request, 'api_mesas.html', {'formulario': formulario})

##########################################################
def sillas(request):
    if request.method == "POST":
        sl = Silla(nombre=request.POST['nombre'], material=request.POST['material'],tipo=request.POST['tipo'],precio=request.POST['precio'])
        sl.save()
        return render(request, "index.html")
    return render(request, "sillas.html")

def buscar_sillas(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        sillas = Silla.objects.filter(nombre__icontains= nombre)
        return render(request, "sillas.html", {'sillas': sillas})
    #elif request.GET['material']:
    #    material = request.GET['material']
    #    material = Mesa.objects.filter(material__icontains= material)
    #    return render(request, "mesas.html", {'material': material})
        
    else:
        respuesta = "No enviaste datos"
    #return render(request, "estudiantes.html") #si no cargo datos se queda en la pag.
    return HttpResponse(respuesta)

def api_sillas(request):
    if request.method == "POST":
        formulario = form_sillas(request.POST)
        print(formulario)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            silla = Silla(nombre= informacion['nombre'], material= informacion['material'], tipo= informacion['tipo'], precio= informacion['precio'])
            silla.save()
            return render(request, 'api_sillas.html')
    else:
        formulario = form_sillas()
    return render(request, 'api_sillas.html', {'formulario': formulario})
######################################

def sofa(request):
    if request.method == "POST":
        sf = Sofa(nombre=request.POST['nombre'], material=request.POST['material'],tipo=request.POST['tipo'],precio=request.POST['precio'])
        sf.save()
        return render(request, "index.html")
    return render(request, "sofa.html")

def buscar_sofa(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        sofas = Sofa.objects.filter(nombre__icontains= nombre)
        return render(request, "sofa.html", {'sofas': sofas})
    #elif request.GET['material']:
    #    material = request.GET['material']
    #    material = Mesa.objects.filter(material__icontains= material)
    #    return render(request, "mesas.html", {'material': material})
        
    else:
        respuesta = "No enviaste datos"
    #return render(request, "estudiantes.html") #si no cargo datos se queda en la pag.
    return HttpResponse(respuesta)

def api_sofa(request):
    if request.method == "POST":
        formulario = form_sillones(request.POST)
        print(formulario)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            sofa = Sofa(nombre= informacion['nombre'], material= informacion['material'], tipo= informacion['tipo'], precio= informacion['precio'])
            sofa.save()
            return render(request, 'api_sofa.html')
    else:
        formulario = form_sillones()
    return render(request, 'api_sofa.html', {'formulario': formulario})

############################################################

def usuario(request):
    if request.method == "POST":
        user = Usuario(nombre=request.POST['nombre'], apellido=request.POST['apellido'],email=request.POST['email'],telefono=request.POST['telefono'])
        user.save()
        return render(request, "index.html")
    return render(request, "usuario.html")

def buscar_usuario(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        usuario = Usuario.objects.filter(nombre__icontains= nombre)
        return render(request, "usuario.html", {'usuario': usuario})
    #elif request.GET['material']:
    #    material = request.GET['material']
    #    material = Mesa.objects.filter(material__icontains= material)
    #    return render(request, "mesas.html", {'material': material})
        
    else:
        respuesta = "No enviaste datos"
    #return render(request, "estudiantes.html") #si no cargo datos se queda en la pag.
    return HttpResponse(respuesta)

def api_usuario(request):
    if request.method == "POST":
        formulario = form_usuario(request.POST)
        print(formulario)
        if formulario.is_valid(): 
            informacion = formulario.cleaned_data
            sofa = Usuario(nombre= informacion['nombre'], apellido= informacion['apellido'], email= informacion['email'], telefono= informacion['telefono'])
            sofa.save()
            return render(request, 'api_sofa.html')
    else:
        formulario = form_usuario()
    return render(request, 'api_usuarios.html', {'formulario': formulario})
