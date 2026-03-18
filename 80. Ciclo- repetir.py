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
print("Ejercicio Nº  80      Sistema de Login con Bloqueo                 ")
print("_________________________________________________________________")
 
USUARIO_CORRECTO = "admin"
CLAVE_CORRECTA  = "danny2026"
MAX_INTENTOS    = 3
intentos        = 0
bloqueado       = False
 
print("  === SISTEMA DE AUTENTICACIÓN ===\n")
 
while True:
    usuario = input("  Usuario   : ")
    clave    = input("  Contraseña: ")
    intentos += 1
 
    if usuario == USUARIO_CORRECTO and clave == CLAVE_CORRECTA:
        print(f"\n  ✓ BIENVENIDO, {usuario.upper()}! Acceso concedido.")
        break
    else:
        restantes = MAX_INTENTOS - intentos
        print(f"  ✗ Credenciales incorrectas. Intentos restantes: {restantes}")
        if intentos >= MAX_INTENTOS:
            bloqueado = True
            break
 
if bloqueado:
    print("  ⛔ CUENTA BLOQUEADA — Contacte al administrador")
print("\n")

print("___________________________________________________")
print("  CÚA , ESTADO MIRANDA 2026                        ")
print("  CURSO DE  PYTHON                                 ")
print("  DEV DEVELOPMENT                                  ")
print("___________________________________________________")