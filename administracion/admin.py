from django.contrib.gis import admin
from .models import Empleado,Camion,Relleno,Ruta,CentroCargaCombustible,ViajeRelleno,CargaCombustible
# Register your models here.

class MyCustomGeoAdmin(admin.OSMGeoAdmin):
    default_lon=-11350000
    default_lat=2519000
    default_zoom=6

admin.site.register(Empleado)
admin.site.register(Camion)
admin.site.register(Relleno,MyCustomGeoAdmin)
admin.site.register(Ruta,MyCustomGeoAdmin)
admin.site.register(CentroCargaCombustible,MyCustomGeoAdmin)
admin.site.register(ViajeRelleno)
admin.site.register(CargaCombustible)
