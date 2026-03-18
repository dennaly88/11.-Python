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
print("       Ejercicio Nº  114 Clase Estudiante con Promedio           ")
print("_________________________________________________________________")



class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def estado(self):
        return "APROBADO" if self.promedio() >= 10 else "REPROBADO"

nombre = input("Nombre del estudiante: ")
e = Estudiante(nombre)
for i in range(3):
    n = float(input(f"  Nota {i+1}: "))
    e.agregar_nota(n)
print(f"Promedio: {e.promedio():.2f} → {e.estado()}")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")