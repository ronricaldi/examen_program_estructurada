def verificar_acceso():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario == "estudiante" and contraseña== "pem2026":
        return "estudiante"
    else:
        return "Usuario y contraseña incorrectos"
