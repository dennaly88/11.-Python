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
print(" Ejercicio Nº  126    Encapsulamiento - Atributos Privados       ")
print("_________________________________________________________________")

class CuentaAhorro:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        self.__tasa = 0.05

    def get_saldo(self):
        return self.__saldo

    def aplicar_interes(self):
        interes = self.__saldo * self.__tasa
        self.__saldo += interes
        print(f"Interés aplicado: +{interes:.2f}. Nuevo saldo: {self.__saldo:.2f}")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

nombre = input("Titular: ")
saldo = float(input("Saldo inicial: "))
cuenta = CuentaAhorro(nombre, saldo)
cuenta.aplicar_interes()
print(f"Saldo final: {cuenta.get_saldo():.2f}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")