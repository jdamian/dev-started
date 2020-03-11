personajes=["uno","dos","tres","cuatro","cinco"]

for personaje in personajes:
    print(personaje)

for valor in range(1,6):
    print(valor)

numeros = list(range(2,11,2))
print(numeros)

cuadrados=[]
for valor in range(1,11):
    cuadrado=valor**2
    cuadrados.append(cuadrado)
print(cuadrados)

misNumeros=list(range(1,21))
print(min(misNumeros))
print(max(misNumeros))
print(sum(misNumeros))

# listas por comprension
misCuadrados=[valor**2 for valor in range(1,11)]
print(misCuadrados)
cubos=[valor**3 for valor in range(1,11)]

#slicing
l = [99, True, “una lista”, [1, 2]]
mi_var = l[0:2] # mi_var vale [99, True]
mi_var = l[0:4:2] # mi_var vale [99, “una lista”]
mi_var = l[1:] # mi_var vale [True, “una lista”]
mi_var = l[:2] # mi_var vale [99, True]
mi_var = l[:] # mi_var vale [99, True, “una lista”]
mi_var = l[::2] # mi_var vale [99, “una lista”]
l[0:2] = [0, 1] # l vale [0, 1, “una lista”, [1, 2]]
l[0:2] = [False] # l vale [False, “una lista”, [1, 2]]
