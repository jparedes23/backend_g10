from rest_framework import serializers
from .models import CategoriasModel, PlatosModel

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields ='__all__'
        #fields =['id','nombre']
        #exclude =['id']

class PlatoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlatosModel
        fields ='__all__'
        depth = 1


class CategoriaConPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields = '__all__'

