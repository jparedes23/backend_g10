from app import app
from controllers.poductos_controller import ProductosController
from flask import request


@app.route("/productos/lista", methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.ListarProductos()

@app.route("/productos/crear", methods=['POST'])
def productosCrear():
    controller = ProductosController()
    return controller.CrearProductos(request.get_json())

@app.route("/productos/eliminar/<int:producto_id>", methods=['DELETE'])
def productoEliminar(producto_id):
    controller = ProductosController()
    return controller.eliminarProducto(producto_id)

@app.route("/productos/actualizar/<int:producto_id>", methods=['PUT'])
def productosActualizar(producto_id):
    controller = ProductosController()
    return controller.actualizarProducto(producto_id, request.json)

@app.route("/productos/buscar/<float:preciosos>", methods=['GET'])
def productoBuscar(preciosos):
    controller = ProductosController()
    return controller.buscarproducto(preciosos)
