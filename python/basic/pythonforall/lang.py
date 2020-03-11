# funciones de orden superior

def saludar(lang):
    def saludar_es():
        print("hola")
    def saludar_en():
        print("hello")
    def saludar_fr():
        print("salut")
    
    # diccionario
    lang_func = {"es": saludar_es,
                "en": saludar_en,
                "fr": saludar_fr}

    return lang_func[lang]

f = saludar("fr") # f contiene una funcion
f()
saludar("fr")()
f = saludar("en")
f()
saludar("en")()
f = saludar("es")
f()
saludar("es")()
print(f)