from Paciente import Paciente

pacientes: list [Paciente] = [
    Paciente("12456321-0","poplio",50,"isapre"),
    Paciente("13234234-6","Piplop",12,"fonasa")
    ]
def menu() -> int:
    print("Menu:\n"
    "1. Agregar paciente\n"
    "2. Editar paciente\n"
    "3. Eliminar paciente\n"
    "4. Imprimir paciente\n"
    "5. Imprimir todos los pacientes\n"
    "0. Salir")
    opcion = leer_numero("Seleccione una opcion: ")
    return opcion

def leer_numero(mensaje : str) -> int:
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("Error: Ingrese un numero")
def main()-> None:
    while True:
        opcion = menu()
        if opcion == 1:
            agregar_paciente()
        elif opcion == 2:
            print("pikachu")
            #editar_paciente()
        elif opcion == 3:
            print("squirtel")
            #eliminar_paciente()
        #elif opcion == 4:
            #print("jijij")
            #imprimir_paciente()
        elif opcion == 5:
            imprimir_pacientes()
        elif opcion == 0:
            break
        else:
            print("Opcion no valida")



def agregar_paciente():
    rut = input("ingrese el rut del paciente: ")
    nombre = input("ingrese el nombre del paciente: ")

    edad = leer_numero("ingrese la edad del paciente: ")
    print("previsiones disponible\n"
    "1. Fonasa\n"
    "2. Isapre\n"
    "3. Particular\n"
    "4. Otro\n" \
    "0. Salir")
    prevision = leer_numero("ingrese su tipo de seguro:")
    if prevision == 1:
        prevision = "Fonasa"
    elif prevision == 2:
        prevision = "Isapre"
    elif prevision == 3:
        prevision = "Particular"
    elif prevision == 4:
        prevision = "otro"
    else:
        prevision = ""
        print("opcion no valida")
        return
    pacientes.append(Paciente(rut,nombre,edad,prevision))

def imprimir_pacientes()-> None:
    if pacientes:
        for paciente in pacientes:
            print(paciente) 
    else:
        print("no hay pacientes registrados")
if __name__ == "__main__":
    main()