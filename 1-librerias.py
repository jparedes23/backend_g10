from camelcase import CamelCase

instancia = CamelCase()

texto ="hola yo deberia ser un camelcase"
resultado=instancia.hump(texto)

print(resultado)


