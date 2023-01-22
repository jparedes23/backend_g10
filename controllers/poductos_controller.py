from models.productos_model import ProdcutosModel
from models.categorias_productos import CategoriasProductosModel
from db import db

class ProductosController:

    def CrearProductos(self, data):
        try:
            print(data)
            producto = ProdcutosModel(data['nombre'], data['precio'])
            db.session.add(producto)
            db.session.commit()

            nuevas_categorias=[]
            for categoria in data['categorias']:
                nueva_categoria = CategoriasProductosModel(producto.id, categoria['categoria_id'])
                nuevas_categorias.append(nueva_categoria)
            db.session.add_all(nuevas_categorias)
            db.session.commit()

            return {
                'data':'No hay ningun error'
            }
        except Exception as e:
            db.session.rollback()
            return{
                'message': 'Internal server error',
                'error': str(e)
            }

    def ListarProductos(self):
        productos = ProdcutosModel.query.all()
        ## creamo una array vacio para luego llenarlo desde el for
        response =[]

        for producto in productos:
            response.append(producto.json())

        return{
            'data': response
        }
    def eliminarProducto(self, producto_id):
        try:
            producto = ProdcutosModel.query.filter_by(id=producto_id).first()
            producto.estado = False
            db.session.commit()
            
            return {
                'message': 'Producto eliminado correctamente'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500

    def actualizarProducto(self, producto_id, data):
        try:
            producto = ProdcutosModel.query.filter_by(id=producto_id).first()
            producto.nombre = data['nombre']
            producto.precio = data['precio']
            db.session.commit()
            return{
                'data': producto.json()
            }, 201
        except Exception as e:
            db.session.rollback()
            return{
                'message': 'Internal server error',
                'error': str(e)
            },500

    def buscarproducto(self, precios):
        try:
            productos = ProdcutosModel.query.filter_by(precio=precios).all()
            response =[]
            for producto in productos:
                response.append(producto.json())
            return{
                'data': response
            }, 200
        except Exception as e:
            return {
                'message': 'Internal server error',
                'error': str(e)
            }, 500