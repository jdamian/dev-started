def mi_funcion(param1, param2):
    """Esta funcion imprime los dos valores pasados 
    como parametros"""
    print param1
    print param2
    return param1+param2

mi_funcion("hola",2)
mi_funcion(param2 = 2, param1 = "Hola")

# valores por defecto
def imprimir(texto, veces = 1):
    print veces * texto

imprimir("Hola")
imprimir("Hola", 2)

# valores variables
def varios(param1, param2, *otros): # otros es tupla
    for val in otros:
        print val

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)

def varios(param1, param2, **otros):    #otros es diccionario
    for i in otros.items():
        print i
varios(1, 2, tercero = 3)

# valor o referencia
# En resumen: los valores mutables se comportan como paso por referencia, y los inmutables como paso por valor.
def f(x, y):
    x = x + 3
    y.append(23)
    print x, y
x = 22
y = [22]
f(x, y)
print x, y

# return varios valores
def f(x, y):
    return x * 2, y * 2 # tupla
a, b = f(1, 2)
