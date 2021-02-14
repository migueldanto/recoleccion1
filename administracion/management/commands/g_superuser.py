from django.core.management.base import BaseCommand
import os
from django.contrib.auth.models import User,Group
#from administracion.models import Empleado


class Command(BaseCommand):
    def handle(self, **options):
        user = os.environ["ADMIN_USER"]
        passw = os.environ["ADMIN_PASS"]
        email="admin@example.com"
        #solo si no existe el usuario agregar
        existe=User.objects.filter(username=user).exists()
        if existe:
            print("usuario por default ya existe")
        else:
            the_user=User.objects.create_superuser(user, email, passw,first_name=str(user).capitalize())
            print("usuario por default creado")
            
        #user2 = "admin1"
        #passw2 = "123456"
        #email2="admin1@example.com"
        #solo si no existe el usuario agregar
        #existe2=User.objects.filter(username=user).exists()
        #from django.contrib.auth.models import Permission

        #permisions2 = Permission.objects.filter(content_type__model="camion")
        #['id', 'name', 'content_type', 'codename']