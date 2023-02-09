from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from .models import CategoriasModel, PlatosModel, UsuarioModel
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import CategoriasSerializers, MostrarPlatoSerializers, CreacionPlatoSerializers, CategoriaConPlatosSerializer, RegistroUsuarioSerializers
# List > Listar (get)
# Create > Crear (post)

class CategoriasApiView(ListCreateAPIView):
    # al utilizar una vista generica que ya no es necesario definir el comportamiento para cuando sea get o post
    # queryset > el comando que utilizara para llamar a la informacion de nuestra base de datos
    # SELECT * FROM categoria;
    queryset = CategoriasModel.objects.all()
    # serializer_class > se define una clase que se encargara de convertir y transformar la informacion que viene desde el cliente y la informacion que enviamos hacia el cliente en dato legibles

    serializer_class = CategoriasSerializers
    # ya no es necesario definir los metodos 'get' y 'post'
    # def get(self):
    #     pass

    # def post(self):
    #     pass

class PlatosApiView(ListCreateAPIView):
    
    queryset= PlatosModel.objects.all()
    #serializer_class= CreacionPlatoSerializers

    def get(self, request: Request):
        # al colocar (:) indicamos que el tipo de datos que sera esa variable en el caso que no le hemos seteado correctamente
        ## request > toda la informacion que viene del cliente
        resultado =  PlatosModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        ## aca llamamos al serializer y ble pasamos la informacion proviniente de la bd y con el parametro many=True indicamos que estamos pasando un arreglo de instancias
        ## no devuelve un diciionario arreglado
        serializador = MostrarPlatoSerializers(instance=resultado, many=True)
        print (serializador.data)
        return Response(data={
            'content': serializador.data
        })
    def post(self, request:Request):
        body = request.data
    # cuando queremos verificar si la informacion es validad entonces utilizamos el paremetro data
        serializador = CreacionPlatoSerializers(data=body)
        valida = serializador.is_valid()

            # si la data pasada al serializador es una data validad se guardara en el atributo valide_data que es un diccionario
        platoExitente=PlatosModel.objects.filter(nombre = serializador.validated_data.get('nombre')).first()
        if platoExitente:
            return Response(data={
                'message':'el plato con nombre {} ya existe csm :) '.format(platoExitente.nombre)
            })

        if valida == False:
            return Response(data={
                'message':' la Informacion es invalidad',
                'content': serializador.errors
            })

        nuevoPlato=serializador.save()
        print(nuevoPlato)
        serializar = MostrarPlatoSerializers(instance=nuevoPlato)

        return Response(data={
            'message': 'Plato creado exitosamente',
            'content': serializar.data
        })

class PlatoDestroyApiView(DestroyAPIView):
    queryset = PlatosModel.objects.all()
    serializer_class = MostrarPlatoSerializers

    def delete(self, request: Request, pk: int):
        print(pk)
        platoEcontrado = PlatosModel.objects.filter(id = pk, disponibilidad = True).first()
        if platoEcontrado is None:
            return Response(data={
                'message': 'el plato no existe'
            })
        platoEcontrado.disponibilidad = False
        platoEcontrado.save()

        return Response(data={
            'message':'plato eliminado exitosamente'
        })

class ListarCategoriaApiView(ListAPIView):
    def get(self, request: Request, pk : int):
        categoriaEncotrada = CategoriasModel.objects.filter(id= pk ).first()
        print(categoriaEncotrada)
        if categoriaEncotrada is None:
            return Response(data={
                'message':'Categoria no Existe'
            })
        
        #print (dir(categoriaEncotrada))
        print(categoriaEncotrada.platos.all())

        serializador = CategoriaConPlatosSerializer(instance=categoriaEncotrada)

        return Response(data={
            'content': serializador.data
        })


class RegistroApiView(CreateAPIView):
    def post(self, request):
        serializador = RegistroUsuarioSerializers(data = request.data)
        validacion = serializador.is_valid()
        if validacion is False:
            return Response(data={
                'message': 'error al crear el usuario',
                'content': serializador.errors
            })
        ## inicializo el nuevo usuario con la informacion validada
        nuevoUsuario = UsuarioModel(**serializador.validated_data)
        ## ahora genero el has de la contraseña
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        ## guardo el usuario en la base de datos
        nuevoUsuario.save()

        return Response (data={
            'message': 'Usuario creado exitosamente'
        }, status=201)


