# es una funcion que recibe una funcion como parametro y devuelve otra funcion

def mi_decorador(funcion):
    def nueva(*args):
        print("Llamada a la funcion ", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nueva

def imp(mensaje):
    print(mensaje)

mi_decorador(imp)("hola")

# los decoradores se ejecutan de abajo hacia arriba
#@otro_decorador
@mi_decorador
def imp(s):
    print(s)

