def crear_lista():
    lista_pacientes = []
    return lista_pacientes


def verificar_digitos(valor):
    while valor.isdigit() == False:
        print("ERRRRRRORRRR TIENEN QUE SER NUMEROS")
        valor = input("Ingrese sus digitos nuevamente por favor.")


def alta(l=crear_lista()):
    a = int(input("Desea dar de alta un paciente? 0 = Si / 1 = no"))
    while a == 0:
        dni = input("Ingrese su DNI por favor.")
        verificar_digitos(dni)
        nombre = input("Ingrese su nombre por favor.")

        edad = input("Cual es su edad")
        verificar_digitos(edad)

        l.append(dni + "/" + nombre + "/" + edad)
        a = int(input("Desea dar de alta un paciente? 0 = Si / 1 = no"))
    return l