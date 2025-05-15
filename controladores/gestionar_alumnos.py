from clases.alumno import Alumno

def crear_alumno() -> Alumno:
    nie : str = ""
    nombre : str = ""
    apellido : str = ""
    tramo : str = ""
    bilingue_str : str = ""
    bilingue : bool = False

    nie : str = input("Ingrese el NIE del alumno (00000000L): ").strip().upper()
    nombre : str = input("Ingrese el nombre del alumno: ").strip()
    apellido : str = input("Ingrese el apellido del alumno: ").strip()
    tramo : str = input("Ingrese el tramo (0,I,II): ").strip().upper()

    bilingue_str= input("¿Es bilingüe? (s/n): ").strip().lower()

    if bilingue_str == "s":
        bilingue = True
    elif bilingue_str == "n":
        bilingue = False
    else:
        print("Entrada no válida para bilingüe. Se ha tomado como 'No bilingüe'")

    alumno: Alumno = Alumno(nombre, apellido, tramo, bilingue)

    if alumno.validacion_datos_alumno():
        print("El alumno se ha creado correctamente.")
        return alumno
    else:
        print("No se ha podido crear el alumno.")
        return None
