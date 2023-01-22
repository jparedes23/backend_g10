from sqlalchemy import Column, Integer, String, Boolean
from db import db

class CategoriasModel(db.Model):
    __tablename__ ='categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(45), nullable=False)
    estado = Column(Boolean, default=True)

    def __init__(self, nombre):
        self.nombre = nombre
   


    def convJson(self):
        return{
            'id': self.id,
            'nombre':self.nombre,
            'estado':self.estado
           
        }