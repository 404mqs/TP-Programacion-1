
    # Menu
def main():    
    def altaPaciente():
        print("Funcion de alta de paciente")



    def altaTurno ():
        print ("Funcion de alta de turnos")



    def modPaciente():
        print ("Funcion de Modificar Paciente")



    def bajaPaciente():
        print ("Funcion de baja paciente")



    def listaxFecha():
        print ("Funcion de listar x dia/mes")



    def listaPacientes():
        print ("Funcion q printea lista total de pacientes")



    def buscarxDni():
        print ("Función de búsqueda de paciente x DNI, q printee todos los datos")



    def cargaPrueba():
        print ("Funcion de carga de datos de prueba (PREGUNTAR COMO QUIERE Q SEA)")


    def s():
        menuOption = 1
        menuOption = int(input(print("Bienvenido/a, por favor, selecciona de las opciones a continuación para seguir: \n 1 = Alta Paciente \n 2 = Alta Turno \n 3 = Modificar Paciente \n 4 = Baja Paciente \n 5 = Lista por dia/mes \n 6 = Lista Pacientes \n 7 = Búsqueda de turnos por DNI \n 8 = Cargar datos de Prueba \n 0 = Cerrar consola")))
        while menuOption != 0:

            if menuOption == 1:
                altaPaciente()

            if menuOption == 2:
                altaTurno()

            if menuOption == 3:
                altaTurno()

            if menuOption == 4:
                altaTurno()

            if menuOption == 5:
                altaTurno()

            if menuOption == 6:
                altaTurno()

            if menuOption == 7:
                altaTurno()

            if menuOption == 8:
                altaTurno()

            if menuOption < 1 or menuOption > 8:
                menuOption = int(input(print("Ha ingresado un valor incorrecto, ingrese una opción válida: ")))

            menuOption = int(input(print("Para seguir operando, ingrese una de las opciones anteriores, para salir, ingrese '0':")))



    s()