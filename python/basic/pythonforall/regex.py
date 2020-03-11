import re
if re.match("python", "python"):
    print("cierto")

re.match(".ython", "python")
re.match(".ython", "jython")
re.match("...\.", "abc.")
re.match("python|jython|cython", "python")
re.match("(p|j|c)ython", "python")
re.match("[pjc]ython", "python")
re.match("python[0-9]", "python0")
re.match("python[0-9a-zA-Z]", "pythonp")
re.match("python[.,]", "python.")
re.match("python[^0-9a-z]", "python+")

# "\d": un dígito. Equivale a [0-9]
# "\D": cualquier carácter que no sea un dígito. Equivale a [^0-9]
# "\w": cualquier caracter alfanumérico. Equivale a [a-zA-Z0-9_]
# "\W": cualquier carácter no alfanumérico. Equivale a [^a-zAZ0-9_]
# "\s": cualquier carácter en blanco. Equivale a [ \t\n\r\f\v]
# "\S": cualquier carácter que no sea un espacio en blanco. Equivale a [^ \t\n\r\f\v]

#  El carácter + indica que lo que tenemos a la izquierda, sea un carácter como ‘a’, una clase como ‘[abc]’ o un subpatrón como (abc), puede encontrarse una o mas veces.
#  “python+” describiría las cadenas “python”, “pythonn” y “pythonnn”

#  El carácter * es similar a +, pero en este caso lo que se sitúa a su izquierda puede encontrarse cero o mas veces.

#  El carácter ? indica opcionalidad, es decir, lo que tenemos a la izquierda puede o no aparecer (puede aparecer 0 o 1 veces).

#  Finalmente las llaves sirven para indicar el número de veces exacto que puede aparecer el carácter de la izquierda, o bien un rango de veces que puede aparecer. Por ejemplo {3} indicaría que tiene que aparecer exactamente 3 veces, {3,8} indicaría que tiene que aparecer de 3 a 8 veces, {,8} de 0 a 8 veces y {3,} tres veces o mas (las que sean).

#  ^ y $, que indican, respectivamente, que el elemento sobre el que actúan debe ir al principio de la cadena o al final de esta.

#  flags: re.IGNORECASE, re.VERBOSE
#  El valor de retorno de la función será None en caso de que la cadena no
# se ajuste al patrón o un objeto de tipo MatchObject en caso contrario. Este objeto MatchObject cuenta con métodos start y end que devuelven la posición en la que comienza y finaliza la subcadena reconocida y métodos group y groups que permiten acceder a los grupos que propiciaron el reconocimiento de la cadena.
#  Al llamar al método group sin parámetros se nos devuelve el grupo 0 de la cadena reconocida. El grupo 0 es la subcadena reconocida por la expresión regular al completo, aunque no existan paréntesis que delimiten el grupo.
mo = re.match("http://.+\net", "http://mundogeek.net")
print(mo.group())
print(mo.group(0))
print(mo.group(1))
mo = re.match("http://(.+)\(.{3})", "http://mundogeek.net")
print(mo.groups())

# funciones: search, findall, finditer, split, sub

#  Si vamos a utilizar un mismo patrón varias veces nos puede interesar crear un objeto de este tipo y llamar a sus métodos nosotros mismos;de esta forma evitamos que el intérprete tenga que crear un nuevo objeto cada vez que usemos el patrón y mejoraremos el rendimiento de la aplicación. Para crear un objeto RegexObject se utiliza la función compile del módulo, al que se le pasa como parámetro la cadena que representa el patrón que queremos utilizar para nuestra expresión regular y, opcionalmente, una serie de flags de entre los que comentamos anteriormente.

