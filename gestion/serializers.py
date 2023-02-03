from rest_framework import serializers
from .models import CategoriasModel

class CategoriaSerializers(serializers.ModelSerializer):
    class Metas:
        model = CategoriasModel
        fields ='__all__'
        #fields =['id','nombre']
        #exclude =['id']