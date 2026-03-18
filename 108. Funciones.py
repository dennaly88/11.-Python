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
print("       Ejercicio Nº  108 Función Palíndromo                      ")
print("_________________________________________________________________")



def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
    print(f'"{palabra}" ES palíndromo')
else:
    print(f'"{palabra}" NO ES palíndromo')


print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")