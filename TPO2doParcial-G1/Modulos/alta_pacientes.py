import os

def clear():
    os.system("cls")
    print()

def crear_lista():
    lista_pacientes = []
    return lista_pacientes


def verificar_digitos(valor):
    while valor.isdigit() == False:
        print("[!] Error. Los numeros deben ser digitos: ")
        valor = input("[?] Ingrese sus datos nuevamente: ")


def main(l=crear_lista()):
    a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:
        dni = input("[?] Ingrese su DNI por favor: ")
        verificar_digitos(dni)
        nombre = input("[?] Ingrese su nombre por favor: ")

        edad = input("[?] Edad: ")
        verificar_digitos(edad)

        nombre_guion = nombre.replace(" ", "_")
        l = f"{dni} {nombre_guion} {edad}\n"

        try:
            with open("Pacientes.txt", "a") as pacientes:
                pacientes.write(str(l)+"")
        except:
            pacientes = open("Pacientes.txt", "a")
            pacientes.write(str(l)+"\n")

        print()
        a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))


if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")
