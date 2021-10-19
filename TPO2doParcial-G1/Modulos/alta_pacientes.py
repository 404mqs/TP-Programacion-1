import os

def clear():
    os.system("cls")
    print()

def crear_lista():
    lista_pacientes = []
    return lista_pacientes

def main(l=crear_lista()):
    clear()
    a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))
    while a == 0:
        dni = input("[?] Ingrese su DNI por favor: ")
        while dni.isdigit() == False:
            dni = input("[?] Ingrese su DNI correctamente por favor. Solo numeros: ")

        nombre = input("[?] Ingrese su nombre por favor: ")

        edad = input("[?] Edad: ")
        while edad.isdigit() == False:
            edad = input("[?] Ingrese su edad nuevamente: ")


        nombre_guion = nombre.replace(" ", "_")
        l = f"{dni} {nombre_guion} {edad}\n"

        try:
            with open("Pacientes.txt", "a") as pacientes:
                pacientes.write(str(l)+"")
        except:
            pacientes = open("Pacientes.txt", "a")
            pacientes.write(str(l)+"")

        print()
        clear()
        a = int(input("[?] Desea dar de alta un paciente?\n \n[0] = Si\n[1] = No\n\n[?] Opcion: "))


if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")
