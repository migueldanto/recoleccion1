from django.core.management.base import BaseCommand
import os
#from django.contrib.auth.models import User,Group
from administracion.models import Empleado,Camion,Relleno

from django.contrib.gis.geos import Point

nombres=["juan","pedro","jorge","pepe","toño","luis"]
camiones=[12,467,322,55,666,122,23454]
rellenos = [
    {
        "nombre":"San Pablo",
        "direccion":"calle1 y calle2",
        "geom": Point(-99.66204643249512,19.358036531316824)
    },
    {
        "nombre":"Calix",
        "direccion":"calle1 y calle2",
        "geom": Point(-99.69423294067383,19.33349825857123)
    },
    {
        "nombre":"Xona",
        "direccion":"calle1 y calle2",
        "geom": Point(-99.53124046325684,19.402973295869995)
    }
]

class Command(BaseCommand):
    def handle(self, **options):
        
        for item in nombres:
            empleado= Empleado(first_name=item,last_name="N",categoria="empleado",no_empleado="00001")
            empleado.save()

        for item in camiones:
            camion = Camion(no_economico=item,placas="xxxxx",modelo="yyyyy")
            camion.save()
        

        for item in rellenos:
            relleno = Relleno(**item)
            relleno.save()

        print("elementos por default creados")