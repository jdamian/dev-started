########## if
if numero < 0:
print “Negativo”
elif numero > 0:
print “Positivo”
else:
print “Cero”

var = “par” if (num % 2 == 0) else “impar”

######### while
edad=0
while edad <18:
    edad++
    print "felicidades, tienes "+str(edad)

while True:
    entrada = raw_input(“> “)
    if entrada == “adios”:
        break
    else:
        print entrada

salir = False
while not salir:
    entrada = raw_input()
    if entrada == “adios”:
        salir = True
    else:
        print entrada

edad = 0
while edad < 18:
    edad = edad + 1
    if edad % 2 == 0:
        continue
    print “Felicidades, tienes “ + str(edad)

######## for
secuencia = [“uno”, “dos”, “tres”]
for elemento in secuencia:
    print elemento
