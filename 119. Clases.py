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
print("       Ejercicio Nº  119  Clase Agenda de Contactos              ")
print("_________________________________________________________________")


class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado.")

    def buscar(self, nombre):
        return self.contactos.get(nombre, "No encontrado")

    def listar(self):
        for n, t in self.contactos.items():
            print(f"  {n}: {t}")

agenda = Agenda()
agenda.agregar("Carlos", "0414-1234567")
agenda.agregar("María", "0424-7654321")
agenda.listar()
print(agenda.buscar("Carlos"))


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")