import os
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_username(username):
    if len(username) > 10:
        return False
    if re.search(r'\d', username):
        return False
    if re.search(r'[^\w]', username):
        return False
    return True

def validate_filename(filename):
    if len(filename) > 10:
        return False
    if re.search(r'\d', filename):
        return False
    if re.search(r'[^\w\.]', filename):
        return False
    if not re.search(r'\.(txt|pdf|docx|xlsx)$', filename):
        return False
    return True

def create_user():
    while True:
        username = input("Ingrese nombre de usuario a crear: ")
        if not validate_username(username):
            print("Error: El nombre de usuario es inválido")
        elif os.path.exists("/home/" + username):
            print("Error: El usuario ingresado ya existe")
        else:
            os.system("useradd " + username)
            print("Usuario creado")
            break

def delete_user():
    while True:
        username = input("Ingrese nombre de usuario a eliminar: ")
        if not validate_username(username):
            print("Error: El nombre de usuario es inválido")
        elif not os.path.exists("/home/" + username):
            print("Error: El usuario no existe")
        else:
            os.system("userdel -r " + username)
            print("Usuario eliminado")
            break

def create_file():
    while True:
        filename = input("Ingrese nombre de archivo a crear: ")
        if not validate_filename(filename):
            print("Error: El nombre de archivo es inválido")
        elif os.path.exists(filename):
            print("Error: El archivo ya existe")
        else:
            os.system("touch " + filename)
            print("Archivo creado")
            break

def delete_file():
    while True:
        filename = input("Ingrese nombre de archivo a eliminar: ")
        if not validate_filename(filename):
            print("Error: El nombre de archivo es inválido")
        elif not os.path.exists(filename):
            print("Error: El archivo no existe")
        else:
            os.system("rm " + filename)
            print("Archivo eliminado")
            break

while True:
    clear_screen()
    print("========BIENVENIDO ADMIN LINUX========")
    print("a.- Administración de usuarios")
    print("b.- Administración de archivos")
    print("c.- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == 'a':
        while True:
            clear_screen()
            print("========ADMIN USUARIOS========")
            print("a.- Crear usuario")
            print("b.- Eliminar usuario")
            print("c.- Volver")

            subopcion = input("Seleccione una opción: ")

            if subopcion == 'a':
                create_user()
                input("Presione ENTER para regresar al menú de usuarios")
            elif subopcion == 'b':
                delete_user()
                input("Presione ENTER para regresar al menú de usuarios")
            elif subopcion == 'c':
                break
            else:
                input("Opción no válida. Intente otra vez")

    elif opcion == 'b':
        while True:
            clear_screen()
            print("========ADMIN ARCHIVOS========")
            print("a.- Crear archivo")
            print("b.- Eliminar archivo")
            print("c.- Volver")

            subopcion = input("Seleccione una opción: ")

            if subopcion == 'a':
                create_file()
                input("Presione ENTER para regresar al menú de archivos")
            elif subopcion == 'b':
                delete_file()
                input("Presione ENTER para regresar al menú de archivos")
            elif subopcion == 'c':
                break
            else:
                input("Opción no válida. Intente otra vez")

    elif opcion == 'c':
        clear_screen()
        print("Saliendo")
        break

    else:
        input("Opción no válida. Intente otra vez")