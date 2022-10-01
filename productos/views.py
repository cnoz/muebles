from django.shortcuts import render, redirect
from django.http import HttpResponse
from productos.forms import form_mesas, form_sillas, form_sillones, form_usuario, UserRegisterForm, UserEditForm, ChangePasswordForm
from productos.models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def inicio(request):
    return render(request, 'index.html')

##################### mesas  ###################################
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
    #return render(request, "crud_productos/read_mesas.html") #si no cargo datos se queda en la pag.
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

#################################### CRUD sillas  ######################################################################


def create_sillas(request):
    if request.method == 'POST':
        silla=Silla(nombre=request.POST['nombre'], material=request.POST['material'], tipo=request.POST['tipo'], precio=request.POST['precio'])
        silla.save()
        sillas=Silla.objects.all()
        return render(request, "crud_sillas/read_sillas.html", {"sillas":sillas})
    return render(request, 'crud_sillas/create_sillas.html')
    
def read_sillas(request=None):
    sillas= Silla.objects.all()
    return render(request,'crud_sillas/read_sillas.html',{'sillas': sillas})

def update_sillas(request, silla_id):
    sillas = Silla.objects.get(id = silla_id)

    if request.method == 'POST':
        formulario = form_sillas(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            sillas.nombre = informacion['nombre']
            sillas.material = informacion['material']
            sillas.tipo = informacion['tipo']
            sillas.precio = informacion['precio']
            sillas.save()
            sillas = Silla.objects.all() #Trae todo
            return render(request, "crud_sillas/read_sillas.html", {"sillas": sillas})
    else:
        formulario = form_sillas(initial={'nombre': sillas.nombre, 'material': sillas.material, 'tipo': sillas.tipo, 'precio': sillas.precio})
    return render(request,"crud_sillas/update_sillas.html", {"formulario": formulario})



def delete_sillas(request, silla_id):
    silla= Silla.objects.get(id = silla_id)
    silla.delete()

    sillas = Silla.objects.all() #Trae todo
    return render(request, "crud_sillas/read_sillas.html", {"sillas": sillas})


################################  LOGIN  ###############################################################

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
                return render(request, 'login.html', {'form':form})
                #return render(request,'login.html',{'form': form })

        else:
            return render(request, 'login.html', {'form': form})

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):

    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        #form2 = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            #username = form.cleaned_data["username"]
            form.save()
            #redirect("/muebles/login/")
            #return render(request, "home.html")
            return redirect("/productos/login/")
        else:
            return render (request, "registro.html", {'form':form})

    #form = UserCreationForm()
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})

###################### PERFIL ######################################################

@login_required

def editarperfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id= usuario.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render (request, 'home.html')
        else:
            return render (request, 'home.html', {'form':form})
    else:
        form = UserEditForm(initial= {'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name,'last_name': usuario.last_name})
    return render(request, 'editarperfil.html', {'form':form, 'usuario': usuario})


@login_required
def changepass(request):
    usuario = request.user
    if request.method == 'POST':
        #form = PasswordChangeForm (data = request.POST, user= usuario)
        form = ChangePasswordForm (data = request.POST, user= usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'home.html')
    else:
        #form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form':form, 'usuario':usuario})

@login_required
def perfilview(request):
    #usuario = request.user
    #user_basic_info = User.objects.get(id = usuario.id)
    #print(usuario)
    #return render(request, 'perfil.html', {'form':user_basic_info})
    return render(request, 'perfil.html')