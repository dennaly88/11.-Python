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
print("           Ejercicio Nº 76 Juego de Par o Impar                  ")
print("_________________________________________________________________")
 
aciertos = 0
rondas = 0
print("  Adivina si el número es PAR o IMPAR")
 
while True:
    import random
    numero = random.randint(1, 100)
    respuesta = input(f"\n  Número: {numero} → ¿Es PAR o IMPAR? (p/i): ").lower()
    rondas += 1
 
    es_par = numero % 2 == 0
    if (respuesta == "p" and es_par) or (respuesta == "i" and not es_par):
        aciertos += 1
        print("  ✓ ¡Correcto!")
    else:
        correcto = "PAR" if es_par else "IMPAR"
        print(f"  ✗ Incorrecto. Era {correcto}")
 
    continuar = input("  ¿Jugar otra ronda? (s/n): ")
    if continuar.lower() != "s":
        break
 
print(f"\n  Resultado: {aciertos} acierto(s) de {rondas} ronda(s)")
print("\n")


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")