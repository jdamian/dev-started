# funciones anonimas en linea

lista = [1, 2, 3]

lista_par =  filter(lambda n: n % 2.0 ==0, lista)

for x in lista_par:
    print(x)