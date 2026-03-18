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
print("       Ejercicio Nº  125 Clase Abstracta con ABC                 ")
print("_________________________________________________________________")


from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def mostrar(self):
        print(f"{type(self).__name__}: area={self.area():.2f}, "
              f"perímetro={self.perimetro():.2f}")

class Rombo(Forma):
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura
    def area(self):
        return self.lado * self.altura
    def perimetro(self):
        return 4 * self.lado

r = Rombo(5, 4)
r.mostrar()


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")