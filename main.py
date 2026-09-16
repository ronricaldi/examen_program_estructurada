
from validador import verificar_acceso
from validador import menu_estudiante

def main():
    print("Bienvenido al sistema de login INFOCAL: ")
    tipo_cuenta = verificar_acceso()

    if tipo_cuenta== "estudiante":
        menu_estudiante()
    else:
        print("Credenciales incorrectas")
main()
        