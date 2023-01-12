from configuracion import conexion
from sqlalchemy import Column, types

class Categoria(conexion.Model):
    id = Column(type_= types.Integer, autoincrement= True, primary_key=True)
    nombre = Column(type_ = types.String(length=50), nullable= False, unique=True)

    __tablename__ ='categorias'


