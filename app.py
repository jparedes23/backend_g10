from flask import Flask
from os import environ
from configuracion import conexion
from dotenv import load_dotenv
from models.categorias_model import Categoria

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= environ.get('DATABASE_URL')

## inicializa la aplicacion de SQLAlchemy con nuestra app de flask
conexion.init_app(app)

@app.before_first_request
def inicializadora():
    conexion.create_all()

if __name__ == '__main__':
    app.run(debug=True)



