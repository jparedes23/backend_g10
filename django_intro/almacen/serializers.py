from rest_framework import serializers
from .models import ProductosModel, CategoriasModel

class ProductosSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)
    class Meta:
        model= ProductosModel
        fields='__all__'
       # exclude = ['estado']
       #  fields =['nombre', 'precio']

class CategoriasSerializer(serializers.ModelSerializer):

    class Meta:
        model= CategoriasModel
        fields='__all__'
       # exclude = ['estado']
       #  fields =['nombre', 'precio']

    def delete(self):
        self.instance.estado = False
        self.instance.save()
        return self.instance




