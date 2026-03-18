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
print("Ejercicio Nº  130  Composición - Aula con Estudiantes      ")
print("_________________________________________________________________")


class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Aula:
    def __init__(self, grado):
        self.grado = grado
        self.estudiantes = []

    def inscribir(self, est):
        self.estudiantes.append(est)

    def reporte(self):
        print(f"\n=== AULA {self.grado} ===")
        for e in self.estudiantes:
            estado = "✓" if e.nota >= 10 else "✗"
            print(f"  {estado} {e.nombre:20} Nota: {e.nota}")
        prom = sum(e.nota for e in self.estudiantes) / len(self.estudiantes)
        print(f"  Promedio del aula: {prom:.2f}")

aula = Aula("5to Año")
for i in range(3):
    n = input(f"Nombre estudiante {i+1}: ")
    nota = float(input(f"Nota de {n}: "))
    aula.inscribir(Estudiante(n, nota))
aula.reporte()


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")