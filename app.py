from flask import Flask, request
from controllers.poductos_controller import ProductosController
from db import db
from flask_migrate import Migrate

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def index():
    return " Mi aplicaion con Flask"


@app.route("/productos/lista", methods=['GET'])
def productosListar():
    controller = ProductosController()
    return controller.ListarProductos()

@app.route("/productos/crear", methods=['POST'])
def productosCrear():
    controller = ProductosController()
    return controller.create(request.get_json())

if __name__ == '__main__':
    app.run(debug=True)