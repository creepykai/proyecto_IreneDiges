from clases.alumno import Alumno

def crear_alumno() -> Alumno:
    nie : str = ""
    nombre : str = ""
    apellido : str = ""
    tramo : str = ""

    nie : str = input("Ingrese el NIE del alumno (00000000L): ").strip().upper()

