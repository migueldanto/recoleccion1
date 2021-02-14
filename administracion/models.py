from django.contrib.gis.db import models
#from django.contrib.auth.models import User

# Modelos base

class Empleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    categoria = models.CharField(max_length=200,blank=True)
    no_empleado = models.CharField(max_length=100,blank=True)

    #prop1 = models.CharField(max_length=300,blank=True,default="")
    #prop2 = models.CharField(max_length=300,blank=True,default="")
    def __str__(self):
        return self.first_name+" "+ self.last_name

"""
Alguna descripcion
"""
class Camion(models.Model):
    """
    Camiones
    """
    id = models.BigAutoField(primary_key=True)
    no_economico = models.IntegerField(unique=True) 
    placas = models.CharField(max_length=50,blank=True,default="")
    modelo = models.CharField(max_length=100,blank=True,default="")
    def __str__(self):
        return str( self.no_economico )

class Relleno(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    geom = models.PointField()
    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    id = models.BigAutoField(primary_key=True)
    geom = models.LineStringField()
    tiempo_aprox_mins = models.IntegerField(default=0)

    nombre = models.CharField(max_length=200)
    def __str__(self):
        return "Ruta no "+str(self.id)+" ["+ self.nombre+"]"

#sugerido
class CentroCargaCombustible(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    geom = models.PointField()
    def __str__(self):
        return str(self.id)+" - "+ self.nombre

##modelos de relacion
class ViajeRelleno(models.Model):
    id = models.BigAutoField(primary_key=True)
    camion = models.ForeignKey(Camion,models.DO_NOTHING)
    chofer = models.ForeignKey(Empleado,models.DO_NOTHING)
    ruta = models.ForeignKey(Ruta,models.DO_NOTHING)
    relleno = models.ForeignKey(Relleno,models.DO_NOTHING)

    #sugerido
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField() 

    def __str__(self):
        return "Viaje no "+str(self.id)+", relleno ["+self.relleno.nombre+"]"

class CargaCombustible(models.Model):
    id = models.BigAutoField(primary_key=True)
    camion = models.ForeignKey(Camion, models.DO_NOTHING)
    chofer = models.ForeignKey(Empleado,models.DO_NOTHING)
    cargo_en = models.ForeignKey(CentroCargaCombustible,models.DO_NOTHING)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return "Carga combustible no "+str(self.id)
    


#dudas
#- las sugerencias
# todo empleado o personal puede ser un usuario?