from models.productos_model import ProdcutosModel
from db import db

class ProductosController:

    def create(self, data):
        try:
            productos = ProdcutosModel(data['nombre'], data['precio'])
            db.session.add(productos)
            db.session.commit()
            return {
                'data':productos.json()
            }
        except Exception as e:
            return{
                'message': 'Internal server error',
                'error': str(e)
            }

    def ListarProductos(self):
        productos = ProdcutosModel.query.all()
        ## creamo una array vacio para luego llenarlo desde el for
        response =[]

        for producto in productos:
            response.append({
                'id': producto.id,
                'nombre': producto.nombre,
                'precio':producto.precio
            })

        return{
            'data': response
        }