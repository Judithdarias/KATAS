estudiantes = []


def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")

    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Ingrese un número válido.")

    estudiantes.append({
        "nombre": nombre,
        "notas": notas
    })

    print("Estudiante agregado correctamente.")


def quitar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")

    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            estudiantes.remove(estudiante)
            print("Estudiante eliminado.")
            return

    print("Estudiante no encontrado.")


def mostrar_aprobados():
    print("\nEstudiantes aprobados (promedio >= 6):")
    hay_aprobados = False

    for estudiante in estudiantes:
        promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
        if promedio >= 6:
            print(estudiante["nombre"], "- Promedio:", round(promedio, 2))
            hay_aprobados = True

    if not hay_aprobados:
        print("No hay estudiantes aprobados.")


def buscar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a buscar: ")

    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
            print(estudiante["nombre"], "- Promedio:", round(promedio, 2))
            return

    print("Estudiante no encontrado.")


def mostrar_todos():
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    print("\nListado de estudiantes:")
    for estudiante in estudiantes:
        promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
        print(estudiante["nombre"], "- Promedio:", round(promedio, 2))


def menu():
    print("\n----- MENÚ -----")
    print("1. Agregar estudiante")
    print("2. Quitar estudiante")
    print("3. Mostrar estudiantes aprobados")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar todos los estudiantes")
    print("6. Salir")


# BUCLE PRINCIPAL
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        quitar_estudiante()
    elif opcion == "3":
        mostrar_aprobados()
    elif opcion == "4":
        buscar_estudiante()
    elif opcion == "5":
        mostrar_todos()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")