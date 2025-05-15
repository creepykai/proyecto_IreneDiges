from clases.alumno import Alumno

def crear_alumno() -> Alumno:
    nie : str = ""
    nombre : str = ""
    apellido : str = ""
    tramo : str = ""
    bilingue_respuesta : str = ""

    nie : str = input("Ingrese el NIE del alumno (00000000L): ").strip().upper()
    nombre : str = input("Ingrese el nombre del alumno: ").strip()
    apellido : str = input("Ingrese el apellido del alumno: ").strip()
    tramo : str = input("Ingrese el tramo (0,I,II): ").strip().upper()
