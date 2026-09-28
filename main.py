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
def eliminar_paciente()->None:
    paciente=buscar_paciente()
    if paciente:
        paciente_rut = input("esta seguro que quiere eliminar?\n" 
        "Ingrese el RUT del paciente: ")
        if paciente.rut == paciente_rut:
            pacientes.remove(paciente) 
            print("Paciente eliminado")
    else:
        print("Paciente no encontrado")

def editar_paciente()->None:
    paciente = buscar_paciente()
    if paciente:
        print("Menu: \n" \
        "1. Editar Nombre\n" \
        "2. Editar Edad\n" \
        "3. Editar Previsión")
        opcion = leer_numero("Ingrese una opcion")
        if opcion == 1:
            print(f"Nombre actual: {paciente.nombre}")
            nombre = input("Ingrese nuevo nombre: ")
            paciente.nombre = nombre
        elif opcion == 2:
            print(f"Edad actual: {paciente.edad}")
            edad = leer_numero("ingrese nueva edad: ")
            paciente.edad = edad
        elif opcion == 3:
            print(f"prevision actual: {paciente.prevision}")
            print("previsiones disponible\n"
                "1. Fonasa\n"
                "2. Isapre\n"
                "3. Particular\n"
                "4. Otro\n" \
                "0. Salir")
            prevision = leer_numero("ingrese una previsión: ")

            if prevision == 1:
                paciente.prevision = "Fonasa"
            elif prevision == 2:
                paciente.prevision = "Isapre"
            elif prevision == 3:
                paciente.prevision = "Particular"
            elif prevision == 4:
                paciente.prevision = "Otro"
            else:
                print("No se realizaron cambios en la previsión")
    else:
        print("Paciente no encontrado")
def main()-> None:
    while True:
        opcion = menu()
        if opcion == 1:
            agregar_paciente()
        elif opcion == 2:
            print("pikachu")
            editar_paciente()
        elif opcion == 3:
            eliminar_paciente()
        elif opcion == 4:
            imprimir_paciente()
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

def buscar_paciente()->Paciente | None:
    rut = input("ingrese el RUT del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None
def imprimir_paciente()-> None:
    paciente = buscar_paciente()
    if paciente: 
        print(paciente)
    else:
        print("Paciente no encontrado. ")
if __name__ == "__main__":
    main()