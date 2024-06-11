Datos = { "Alumnos": []}

def mostrar_opciones():
    print("1. Mostrar datos de cada alumno")
    print("2. Modificar datos de un alumno")
    print("3. Agregar un alumno")
    print("4. Expulsar un alumno")
    print("5. Salir")

def mostrar_datos():
    for i, alumno in enumerate(Datos["Alumnos"], start=1):
        print(f"Alumno {i}: {alumno}")

def modificar_datos():
    mostrar_datos()
    index = int(input("Ingrese el número del alumno que desea modificar: ")) - 1
    if 0 <= index < len(Datos["Alumnos"]):
        alumno = Datos["Alumnos"][index]
        print("Datos actuales del alumno:", alumno)
        campo = input("Ingrese el campo que desea modificar (Nombre, Apellido, DNI, Fecha de nacimiento, Tutor, Notas, Faltas, Amonestaciones): ")
        if campo in alumno:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            if campo == "Notas" or campo == "Faltas" or campo == "Amonestaciones":
                nuevo_valor = int(nuevo_valor)  
            alumno[campo] = nuevo_valor
        else:
            print("Campo no válido.")
    else:
        print("Índice no válido.")

def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    tutor = input("Ingrese el nombre y apellido del tutor: ")
    notas = list(map(int, input("Ingrese todas las notas del alumno (separadas por espacios): ").split()))
    faltas = int(input("Ingrese la cantidad de faltas: "))
    amonestaciones = int(input("Ingrese la cantidad de amonestaciones: "))
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "amonestaciones": amonestaciones
    }
    Datos["Alumnos"].append(nuevo_alumno)
    print("Alumno agregado exitosamente.")

def expulsar_alumno():
    mostrar_datos()
    index = int(input("Ingrese el número del alumno que desea expulsar: ")) - 1
    if 0 <= index < len(Datos["Alumnos"]):
        Datos["Alumnos"].pop(index)
        print("Alumno expulsado exitosamente.")
    else:
        print("Índice no válido.")

def principal():
    while True:
        mostrar_opciones()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            mostrar_datos()
        elif opcion == 2:
            modificar_datos()
        elif opcion == 3:
            agregar_alumno()
        elif opcion == 4:
            expulsar_alumno()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    principal()