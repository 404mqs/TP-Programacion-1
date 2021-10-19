import os

def clear():
    os.system("cls")
    print()

def main():
    clear()  
    f = open("Pacientes.txt", "r")
    lista_nombres = []
    lista_dni = []
    lista_edad = []

    for linea in f:
        lista = linea.split()
        nombre = lista[1].replace("_", " ")
        dni = lista[0]
        edad = lista[2]
        lista_nombres.append(nombre)
        lista_dni.append(dni)
        lista_edad.append(edad)

    f.close()

    print("[+] Lista de pacientes registrados:\n")
    for i, valor in enumerate((lista_nombres)):
            print(f"Paciente {i}: {valor} -- DNI: {lista_dni[i]} -- {lista_edad[i]} AÑOS")

    print()
    input("[+] Presione enter para continuar...")


if __name__ == "main":
    print("Ejecutando directamente")
    main()

else:
    print("Ejecutando desde script")
