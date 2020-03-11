# Iteraciones de orden superior sobre listas, funciones map, filter y reduce

lista = [1, 2, 3]

# map(function, sequence[,sequence,..])
# aplica una funcion a cada elemento de la secuencia, devuelve una lista

def cuadrado(n):
    return n ** 2

lista_cuadrados = map( cuadrado, lista)

print(lista)
for x in lista_cuadrados:
    print(x)

# filter(function, sequence)
# verifica que cumpla una funcion

def es_par(n):
    return (n % 2.0 == 0)

lista_par = filter(es_par, lista)
for x in lista_par:
    print(x)

# reduce(function, sequence[, initial])
# deja un solo valor

def sumar(x, y):
    return x+y

# lista_reducida = reduce(sumar, lista)
