
from django.urls import path
from productos.views import *
from django.contrib.auth.views import LogoutView

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
        path('api_usuario/', api_usuario),
        path('read_mesas/', read_mesas),
        path('create_mesas/', create_mesas),
        path('update_mesas/<mesa_id>', update_mesas),
        path('delete_mesas/<mesa_id>', delete_mesas),

        path('read_sillas/', read_sillas),
        path('create_sillas/', create_sillas),
        path('update_sillas/<silla_id>', update_sillas),
        path('delete_sillas/<silla_id>', delete_sillas),

        path('read_sofa/', read_sofa),
        path('create_sofa/', create_sofa),
        path('update_sofa/<sofa_id>', update_sofa),
        path('delete_sofa/<sofa_id>', delete_sofa),

        path('read_usuario/', read_usuario),
        path('create_usuario/', create_usuario),
        path('update_usuario/<usuario_id>', update_usuario),
        path('delete_usuario/<usuario_id>', delete_usuario),


        path('login/', login_request),
        path('registro/', registro),
        path('logout/', LogoutView.as_view(template_name = 'home2.html'), name = 'logout'), #cambie home.html x home2.html
        path('perfil/editarperfil/', editarperfil),
        path('perfil/', perfilview),
        path('perfil/changepass/', changepass),
        path('perfil/changeAvatar/', AgregarAvatar),
        path('compras/', compras),
        path('comprass/', compras2),      
        path('compra_silla/', compra_silla), 
        path('compra_mesa/', compra_mesa),     
        path('compra_sofa/', compra_sofa),    
        path('compra_usuario/', compra_usuario), 
        path('acceso/',acceso)     
]
