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
print("          Ejercicio Nº  124 Herencia Múltiple                    ")
print("_________________________________________________________________")


class Volador:
    def volar(self):
        return f"{self.nombre} puede volar"

class Nadador:
    def nadar(self):
        return f"{self.nombre} puede nadar"

class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre

    def presentar(self):
        print(self.volar())
        print(self.nadar())

donald = Pato("Donald")
donald.presentar()
print(f"MRO: {[c.__name__ for c in Pato.__mro__]}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")