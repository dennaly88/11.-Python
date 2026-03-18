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
print("       Ejercicio Nº  116 Clase con Atributos de Clase            ")
print("_________________________________________________________________")

 
class Empleado:
    empresa = "TechVenezuela C.A."
    contador = 0

    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        Empleado.contador += 1

    def mostrar(self):
        print(f"[{self.empresa}] {self.nombre} - {self.cargo}")

e1 = Empleado("Luis", "Programador")
e2 = Empleado("Ana",  "Diseñadora")
e1.mostrar()
e2.mostrar()
print(f"Total empleados: {Empleado.contador}")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")