from rest_framework import serializers
from .models import CategoriasModel, PlatosModel, UsuarioModel

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriasModel
        fields ='__all__'
        #fields =['id','nombre']
        #exclude =['id']

class MostrarPlatoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlatosModel
        fields ='__all__'
        depth = 1


class CreacionPlatoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlatosModel
        exclude =['disponibilidad']


class CategoriaConPlatosSerializer(serializers.ModelSerializer):
    #platos biene desde el modelo PlatosModel-> related_name='platos'
    #platos = CreacionPlatoSerializers(many=True)

    #
    #
    info_adicional = CreacionPlatoSerializers(many=True, source='platos')
    class Meta:
        model = CategoriasModel
        fields = '__all__'

class RegistroUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        fields ='__all__'
        model = UsuarioModel
    # extra_kwargs > 
        extra_kwargs ={
            'password':{
                'write_only': True
            }
        }



