def verificar_acceso():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario == "estudiante" and contraseña== "pem2026":
        return "estudiante"
    else:
        return "Usuario y contraseña incorrectos"


def menu_estudiante ():
    while True:
        print("*****MENU ESTUDANTE*****")
        print("1. Mostrando Informacion")
        print("2. Ver informacion de clases")
        print("3. Salir del menu estudainte")
        opcion= input("Ingrese la opcion elegida: ")
        if opcion == ("1"):
            print("Esta es la informacion registrada en el sistema de estudainte...")
        elif opcion==("2"):
            print("registro de materias....")
        elif opcion==("3"):
            print("Saliendo del menu de estududiante.....")