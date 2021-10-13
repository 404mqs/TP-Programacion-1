import os
import Modulos.menu as menu

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
            print(f"[+] Bienvenido {user.upper()}. Abriendo menu...")
            print()

            menu.main()
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





