from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
## PermissionsMixin sirve para relacionar la tabla auth_user con las tablas de permiso, tanto de la auth_permission como la de group_permissions
from .auth_manager import UsuarioManager


class CategoriasModel (models.Model):
    id= models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table ='categorias'


    ordering =['nombre']

class PlatosModel(models.Model):

    nombre = models.CharField(max_length=50, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    #relater sirve para poder acceder a todos los registros desde la otra entidad es decir desde categoria y acceder a todos sus platos
    # si no se define su valor sera puesto por django con el nombre de la clase todo en minusculas 'platosmodel_Set'
    categoria = models.ForeignKey(to = CategoriasModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')

    class Meta:
        db_table ='platos'
#como vamos amodificar el comportamiento de la tabla auth_user de Django entonmces tenemos que modificar su herencia
class UsuarioModel(AbstractBaseUser , PermissionsMixin):
## AbstractBaseUser -> me permite modificar todo del modelo auth_user mientras
##AbstracUser solamente me permite agregar nuevas columnas
    id = models.AutoField(primary_key=True,  unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password =models.TextField(null=False)# -> tiene que ser password
    tipoUsuario= models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('MOZO','MOZO'),
        ('CLIENTE','CLIENTE')
    ])

    ## propiedades netas para el panel administrativos
         # sirve para indicar si el usuario que quiere acceder pertenece o no al equipo de trabajo
    is_staff =  models.BooleanField(default=True)
         # sirve para indicar si el usuario es un usuario esta activo en la empresa
    is_active = models.BooleanField(default=True)
         # sirve para indicar la fecha en la que se creo
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
         # SIRVE PARA EL PANEL ADMINISTRATIVO PARA INDICAR CUAL ES LA COMUNNA
    USERNAME_FIELD = 'correo'
         # SON LAS COLUMNAS O LOS ATRAIBUTOS REQUERIDOS AL MOMENTO DE CREAR EL SUPERUSARIO POR CONSOLA
    REQUIRED_FIELDS =['nombre', 'apellido','tipoUsuario']

    # hacemos uso de UsuarioManager que viene de auth_manager.py
    objects = UsuarioManager()
    class Meta:
        db_table = 'usuarios'


## borrar la bd restaurante
## agregar PermissionsMixin
## python manage.py makemigrations
## python manage.py migrate gestion
## porque estamos obligando a django que primero ejecute las migraciones de gestion 
## python manage.py migrate 
## mirar la bd que se vvolvio 
##