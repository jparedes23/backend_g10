from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductosModel, CategoriasModel
from .serializers import ProductosSerializer, CategoriasSerializer
from rest_framework import generics
from rest_framework.response import Response


def renderHtml(request):
    return HttpResponse("Este es un texo cualquiera")

def buscarProducto(request, producto_id):
    producto = ProductosModel.objects.filter(id=producto_id).first()
    print (producto)
    return HttpResponse(f'Producto encontrado {producto.nombre} y el precio es {producto.precio}')

class ProductosView(generics.ListAPIView):
    queryset = ProductosModel.objects.all()
    serializer_class = ProductosSerializer

class CategoriasView(generics.GenericAPIView):
    queryset = CategoriasModel.objects.all()
    serializer_class= CategoriasSerializer

    def get(self, request):
        try:

            record = self.get_queryset()
            serializer = self.get_serializer(record, many=True)
            print(record)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'message': 'Internal server error'
            })


    def post (self, request):
        try:
            categoria = self.get_serializer(data=request.data)
            if categoria.is_valid():
                categoria.save()
                return Response(categoria.data)
            print(categoria.errors)
            erros = 'faltan campos'
            for campo in categoria.errors:
                error = error +' '+ campo + ','
            return Response({
                'message': error
            })
        except Exception as e:
            return Response({
                'message': 'Internal server error'
            })



class ActualizarCategoriasView(generics.GenericAPIView):
    queryset = CategoriasModel.objects.all()
    serializer_class = CategoriasSerializer

    def get(self, request, categoria_id):
        try:
            record = self.get_queryset().get(id=categoria_id)
            serializer = self.get_serializer(record)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'message':'Internal Server error'
            })

    def put(self, request, categoria_id):
        try:
            categoria = self.queryset().get(id=categoria_id)
            serializer = self.get_serializer(categoria, data=request.data)
            if serializer.is_valid():
                updated = serializer.update(categoria, serializer.validated_data)
                nuevo_serializador = self.get_serializer(updated)
                print(updated)
            return Response(nuevo_serializador.data)
            
        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            })

    def delete(self, request, categoria_id):
        try:
            categoria = self.get_queryset().get(id=categoria_id)
            serializador = self.get_serializer(categoria)
            serializador.delete()
            return Response({
                'message':'Categoria eliminada correctamente'
            })

        except Exception as e:
            return Response({
                'message': 'Internal server error',
                'error': str(e)
            })