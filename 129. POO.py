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
print("Ejercicio Nº  129 Herencia - Sistema de Empleados                ")
print("_________________________________________________________________")


class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class Empleado(Persona):
    def __init__(self, nombre, cedula, cargo, salario):
        super().__init__(nombre, cedula)
        self.cargo = cargo
        self.salario = salario

    def info(self):
        print(f"{'='*40}")
        print(f"  Nombre  : {self.nombre}")
        print(f"  Cédula  : {self.cedula}")
        print(f"  Cargo   : {self.cargo}")
        print(f"  Salario : Bs. {self.salario:,.2f}")
        print(f"{'='*40}")

nombre  = input("Nombre: ")
cedula  = input("Cédula: ")
cargo   = input("Cargo: ")
salario = float(input("Salario: "))
emp = Empleado(nombre, cedula, cargo, salario)
emp.info()

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")