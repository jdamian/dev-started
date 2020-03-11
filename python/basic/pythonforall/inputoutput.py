import sys

nombre = raw_input("como te  llamas?: ")
print("bienvenido, "+nombre)

try:
    edad = raw_input("cuantos años tienes?: ")
    dias = int(edad) * 365
    print("has vivido " + str(dias) + " dias.")
except ValueError as ve:
    print("no es un numero")

if(len(sys.argv) >1 ):
    print("abriendo " + sys.argv[1])
else:
    print("debes indicar el nombre del archivo como parametro")

# salida estandar