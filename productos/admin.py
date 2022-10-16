from django.contrib import admin
from .models import *
# Register your models here.

class MesaAdmin(admin.ModelAdmin):
    list_display=('nombre', 'material', 'tipo', 'precio')
    search_fields=('nombre', 'precio','tipo')
    list_filter=('material',)
    
admin.site.register(Mesa, MesaAdmin)
admin.site.register(Silla)
admin.site.register(Sofa)
admin.site.register(Usuario)
admin.site.register(Avatar)