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
print("       Ejercicio Nº  123 Polimorfismo con Métodos                ")
print("_________________________________________________________________")


class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        pass

class PorHora(Trabajador):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa
    def calcular_pago(self):
        return self.horas * self.tarifa

class Asalariado(Trabajador):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario
    def calcular_pago(self):
        return self.salario

trabajadores = [PorHora("Luis", 40, 25), Asalariado("Ana", 3000)]
for t in trabajadores:
    print(f"{t.nombre}: Bs. {t.calcular_pago():.2f}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")