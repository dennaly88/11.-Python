print("___________________________________________________")
print("___________________________________________________")
print("  DANNY JOSE JIMENEZ GUTIERREZ                     ")
print("  TELEFONO :0424-281-44-55                         ")
print("  CORREO : [DENNALY88@GMAIL.COM]                   ")
print("  INGENIERO EN INFORMÁTICA                         ")
print("___________________________________________________")
print("___________________________________________________")
print("\n")


print("_________________________________________________________________")
print("            Ejercicio Nº  128  Patrón Singleton                  ")
print("_________________________________________________________________")


class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.debug = False
            cls._instancia.idioma = "es"
        return cls._instancia

    def mostrar(self):
        print(f"Debug: {self.debug} | Idioma: {self.idioma}")

c1 = Configuracion()
c2 = Configuracion()
c1.debug = True
c2.mostrar()  
print(f"c1 is c2: {c1 is c2}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")