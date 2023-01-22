from db import db
from sqlalchemy import Column, Integer, String, Float, Boolean

class ProdcutosModel(db.Model):
    __tablename__='prodcutos'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    precio = Column(Float, nullable=False)
    estado = Column(Boolean, default=True)


## metodo primitivo y magico

    def __init__(self, nombre, precio, ):
        self.nombre= nombre
        self.precio= precio
    
    
### creamos methodo json para comvertir a un diccionario

    def json(self):
        return{
            'id':self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'estado': self.estado
        }