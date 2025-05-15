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

    alumno: Alumno = Alumno(nie, nombre, apellido, tramo, bilingue)

    if alumno.validacion_datos_alumno():
        print("El alumno se ha creado correctamente.")
        return alumno
    else:
        print("No se ha podido crear el alumno.")
        return None

def modificar_alumno(alumno: Alumno) -> None:
    nuevo_nombre: str = ""
    nuevo_apellido: str = ""
    nuevo_tramo: str = ""
    nuevo_str_bilingue: str = ""
    nombre_final: str = ""
    apellidos_final: str = ""
    tramo_final: str = ""
    nuevo_bilingue: bool = alumno.bilingue  # valor actual
    bilingue_final: bool = alumno.bilingue

    nuevo_nombre = input("Ingrese el nuevo nombre del alumno / Dejar vacío si no se quiere modificar: ").strip()
    nuevo_apellido = input("Ingrese el nuevo apellido del alumno / Dejar vacío si no se quiere modificar: ").strip()
    nuevo_tramo = input("Introduce el nuevo tramo: (0, I, II) / Dejar vacío si no se quiere modificar: ").strip().upper()
    nuevo_str_bilingue = input("¿Es bilingüe? (s/n) / Dejar vacío si no se quiere modificar: ").strip().lower()

    nombre_final = alumno.nombre if nuevo_nombre == "" else nuevo_nombre
    apellidos_final = alumno.apellidos if nuevo_apellido == "" else nuevo_apellido
    tramo_final = alumno.tramo if nuevo_tramo == "" else nuevo_tramo

    if nuevo_str_bilingue == "s":
        bilingue_final = True
    elif nuevo_str_bilingue == "n":
        bilingue_final = False
    else:
        bilingue_final = alumno.bilingue

    alumno_temporal: Alumno = Alumno(alumno.nie, nombre_final, apellidos_final, tramo_final, bilingue_final)

    if alumno_temporal.validacion_datos_alumno():
        alumno.modificar_datos(nombre_final, apellidos_final, tramo_final, bilingue_final)
        print("El alumno se ha modificado correctamente.")
    else:
        print("No se han guardado los cambios porque los datos no son válidos.")

