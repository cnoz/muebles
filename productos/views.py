from django.shortcuts import render, redirect
from django.http import HttpResponse
from productos.forms import form_mesas, form_sillas, form_sillones, form_usuario, UserRegisterForm
from productos.models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    return render(request, 'index.html')

##################### mesas         ###################################
@login_required
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

####################  sillas        #####################################

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
##################  sofa        ####################

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

################# usuario ###########################################

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

#################################### CRUD mesas  ######################################################################



def create_mesas(request):
    if request.method == 'POST':
        mesa=Mesa(nombre=request.POST['nombre'], material=request.POST['material'], tipo=request.POST['tipo'], precio=request.POST['precio'])
        mesa.save()
        mesas=Mesa.objects.all()
        return render(request, "crud_productos/read_mesas.html", {"mesas":mesas})
    return render(request, 'crud_productos/create_mesas.html')
    
def read_mesas(request=None):
    mesas= Mesa.objects.all()
    return render(request,'crud_productos/read_mesas.html',{'mesas': mesas})

def update_mesas(request, mesa_id):
    mesas = Mesa.objects.get(id = mesa_id)

    if request.method == 'POST':
        formulario = form_mesas(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            mesas.nombre = informacion['nombre']
            mesas.material = informacion['material']
            mesas.tipo = informacion['tipo']
            mesas.precio = informacion['precio']
            mesas.save()
            mesas = Mesa.objects.all() #Trae todo
            return render(request, "crud_productos/read_mesas.html", {"mesas": mesas})
    else:
        formulario = form_mesas(initial={'nombre': mesas.nombre, 'material': mesas.material, 'tipo': mesas.tipo, 'precio':mesas.precio})
    return render(request,"crud_productos/update_mesas.html", {"formulario": formulario})



def delete_mesas(request, mesa_id):
    mesa= Mesa.objects.get(id = mesa_id)
    mesa.delete()

    mesas = Mesa.objects.all() #Trae todo
    return render(request, "crud_productos/read_mesas.html", {"mesas": mesas})

##  LOGIN ###

def login_request(request):    
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)    
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user , password = pwd)

            if user is not None:
                login(request, user )
                return  render(request, 'index.html')
            
            else:
                return render(request, 'productos/login.html', {'form':form})
                #return render(request,'login.html',{'form': form })

        else:
            return render(request, 'productos/login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form2 = UserRegisterForm(request.POST)
        print(form2)
        if form2.is_valid():
            #username = form.cleaned_data["username"]
            form2.save()
            #redirect("/muebles/login/")
            #return render(request, "home.html")
            return redirect("/productos/login/")

    #form = UserCreationForm()
    form2 = UserRegisterForm()
    return render(request, "registro.html", {'form1': form2})
