

try:
    f = file("archivo.txt")
except:
    print("el archivo no existe")

try:
    num = int("3a")
    print(no_existe)
except NameError:
    print("La variable no existe")
except ValueError:
    print("El valor no es un numero")
except (NameError, ValueError):
    print("ocurrio un error")
else:
    print("todo esta bien")
finally:
    print("limpiando")

class MiError(Exception):
    def __init__(self, valor):
        super().__init__(self, valor)
        self.valor = valor
    def __str__(self):
        return "Error " + str(self.valor)

resultado = 90
try:
    if resultado > 20:
        raise MiError(33)

except MiError as e:
    print(e)
