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
print("         Ejercicio Nº  120  Clase Círculo con Propiedades       ")
print("_________________________________________________________________")


import math

class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def area(self):
        return math.pi * self._radio ** 2

    @property
    def circunferencia(self):
        return 2 * math.pi * self._radio

r = float(input("Radio del círculo: "))
c = Circulo(r)
print(f"Área: {c.area:.4f}")
print(f"Circunferencia: {c.circunferencia:.4f}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")