from django.db import models


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
    categoria = models.ForeignKey(to = CategoriasModel, on_delete=models.PROTECT, db_column='categoria_id')
