lista = [0, 1, 2, 3]
lista_cuadrado = [n ** 2 for n in lista]
lista_par = [n for n in lista if n % 2.0 ==0]

m = ["a","b"]

n = [ s* v for s in m
            for v in lista
            if v >0 ]