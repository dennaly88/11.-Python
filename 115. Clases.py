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
print("         Ejercicio Nº  115 Clase Vehículo                        ")
print("_________________________________________________________________")


class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")

    def info(self):
        estado = "Encendido" if self.encendido else "Apagado"
        print(f"{self.marca} {self.modelo} ({self.año}) - {estado}")

v = Vehiculo("Toyota", "Corolla", 2020)
v.info()
v.encender()
v.info()


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")