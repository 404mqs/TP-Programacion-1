import os
from Modulos.alta_pacientes import main as altapacientes
from Modulos.listar_pacientes import main as listarpacientes
from Modulos.baja_pacientes import main as bajapacientes

# Funciones

def clear():
    os.system("cls")
    print()

def registrar(user, password):
    try: 
        with open("Usuarios.txt", "a") as usuarios:
            with open("Passwords.txt", "a") as contras:     
                usuarios.write(f"{user} ")
                contras.write(f"{password} ")
    except:
        usuarios = open("Usuarios.txt", "a")
        contras = open("Passwords.txt", "a")
        usuarios.write(f"{user} ")
        contras.write(f"{password} ")

def iniciar_sesion(user, password, usersdb, passwordsdb):
    if user in usersdb:
        pos = usersdb.index(user)
        if passwordsdb[pos] == password:
            print("[+] Se inicio sesion correctamente!")
            print()
            return True

# Programa Principal

clear()
opcion = int(input("[1] Registro \n[2] Login \n\n[?] Opcion: "))

print()
while opcion not in [1, 2]:
    clear()
    opcion = int(input("[1] Registro \n[2] Login \n\n[?] Opcion: "))

while opcion in [1, 2]:
    clear()    
    if opcion == 1:
        user = input("[?] Nombre de usuario: ")
        password = input("[?] Contrasena: ")

        registrar(user, password)
        print()
        clear()
        print("[+] Registrado correctamente!")
        print()
        opcion = int(input("[1] Registro \n[2] Login \n\n[?] Opcion: "))

    if opcion == 2:  
        clear()    
        
        try:  
            with open("Usuarios.txt", "r") as usuarios:
                with open("Passwords.txt", "r") as contras:     
                    lista_users = usuarios.read().split()
                    lista_passwords = contras.read().split()
        except:
                usuarios = open("Usuarios.txt", "a")
                contras = open("Passwords.txt", "a")
                usuarios.write(f" ")
                contras.write(f" ")
                with open("Usuarios.txt", "r") as usuarios:
                    with open("Passwords.txt", "r") as contras:
                        lista_users = usuarios.read().split()
                        lista_passwords = contras.read().split()

        user = input("[?] Nombre de usuario: ")
        password = input("[?] Contrasena: ")

        inicio = iniciar_sesion(user, password, lista_users, lista_passwords)

        if inicio:
            clear()
            menuOption = int(input(F"[+] Bienvenido/a {user.upper()}, por favor, selecciona de las opciones a continuación para seguir: \n\n[1] - Alta Paciente \n[2] - Alta Turno \n[3] - Modificar Paciente \n[4] - Baja Paciente \n[5] - Lista por dia/mes \n[6] - Lista Pacientes \n[7] - Búsqueda de turnos por DNI \n[8] - Cargar datos de Prueba \n[0] - Cerrar consola\n\n[?] Opcion: "))
            while menuOption != 0:
                if menuOption == 1:
                    altapacientes()

                if menuOption == 2:
                    print()

                if menuOption == 3:
                    print("Alta turno")

                if menuOption == 4:
                    bajapacientes()

                if menuOption == 5:
                    print("Alta turno")

                if menuOption == 6:
                    listarpacientes()

                if menuOption == 7:
                    print("Alta turno")

                if menuOption == 8:
                    print("Alta turno")

                if menuOption < 1 or menuOption > 8:
                    menuOption = int(input("[!] Ha ingresado un valor incorrecto, ingrese una opción válida: "))
                clear()
                menuOption = int(input(F"[+] Bienvenido/a {user.upper()}, por favor, selecciona de las opciones a continuación para seguir: \n\n[1] - Alta Paciente \n[2] - Alta Turno \n[3] - Modificar Paciente \n[4] - Baja Paciente \n[5] - Lista por dia/mes \n[6] - Lista Pacientes \n[7] - Búsqueda de turnos por DNI \n[8] - Cargar datos de Prueba \n[0] - Cerrar consola\n\n[?] Opcion: "))

            break

        else:
            clear()
            print("[!] Uno o ambos datos ingresados son incorrectos. Intente nuevamente.")
            print()
            opcion = int(input("[1] Registro \n[2] Login \n\n[?] Opcion: "))

            while opcion not in [1, 2]:
                clear()
                print("[!] Uno o ambos datos ingresados son incorrectos. Intente nuevamente.")
                print()
                opcion = int(input("[1] Registro \n[2] Login \n\n[?] Opcion: "))





