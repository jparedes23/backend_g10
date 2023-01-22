from os import  listdir
from pathlib import Path

path_parent = Path("./routers")

for module in listdir(path_parent):
    #print(module)
    if 'router' in module:
        #para que ya no nos muestre __init__ ni __pycache__
        #print(module)
        __import__(
            f'routers.{module[:-3]}',
            locals(),
            globals()
        )
