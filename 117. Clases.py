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
print("               Ejercicio Nº  117 Clase Pila                      ")
print("_________________________________________________________________")


class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return "Pila vacía"

    def tope(self):
        return self.elementos[-1] if self.elementos else None

    def esta_vacia(self):
        return len(self.elementos) == 0

p = Pila()
p.push(10); p.push(20); p.push(30)
print(f"Tope: {p.tope()}")
print(f"Pop:  {p.pop()}")
print(f"Pop:  {p.pop()}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")