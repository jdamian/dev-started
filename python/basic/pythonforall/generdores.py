lista = [0,1,2,3,4]
lista_cuadrado = (n ** 2 for n in lista)

# generador
def mi_generador(n, m, s):
    while(n <= m):
        yield n
        n += s

for n in mi_generador(0,5,1):
    print(n)

lista_nueva = list(mi_generador)