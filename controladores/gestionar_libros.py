from clases.libro import Libro

def crear_libro() -> Libro:
    isbn: str = ""
    titulo: str = ""
    editorial: str = ""
    materia: str = ""
    curso: str = ""

    isbn = input("Introduce el ISBN del libro (13 dígitos): ").strip()
    titulo = input("Introduce el título del libro: ").strip()
    editorial = input("Introduce la editorial: ").strip()
    materia = input("Introduce la materia: ").strip()
    curso = input("Introduce el curso: ").strip()

    libro: Libro = Libro(isbn, titulo, editorial, materia, curso)

    if libro.validar_datos_libro():
        print("El libro se ha creado correctamente.")
        return libro
    else:
        print("o se ha podido crear el libro. Revisa los datos introducidos.")
        return None


def modificar_libro(libro: Libro) -> None:
    nuevo_titulo: str = ""
    nuevo_editorial: str = ""
    nuevo_materia: str = ""
    nuevo_curso: str = ""

    titulo_final: str = ""
    editorial_final: str = ""
    materia_final: str = ""
    curso_final: str = ""

    nuevo_titulo = input("Introduce el nuevo título / Dejar vacío si no se quiere modificar: ").strip()
    nuevo_editorial = input("Introduce la nueva editorial / Dejar vacío si no se quiere modificar: ").strip()
    nuevo_materia = input("Introduce la nueva materia / Dejar vacío si no se quiere modificar: ").strip()
    nuevo_curso = input("Introduce el nuevo curso / Dejar vacío si no se quiere modificar: ").strip()

    titulo_final = libro.titulo if nuevo_titulo == "" else nuevo_titulo
    editorial_final = libro.editorial if nuevo_editorial == "" else nuevo_editorial
    materia_final = libro.materia if nuevo_materia == "" else nuevo_materia
    curso_final = libro.curso if nuevo_curso == "" else nuevo_curso

    libro_temporal: Libro = Libro(libro.isbn, titulo_final, editorial_final, materia_final, curso_final)

    if libro_temporal.validar_datos_libro():
        libro.modificar_datos(titulo_final, editorial_final, materia_final, curso_final)
        print("El libro se ha modificado correctamente.")
    else:
        print("No se han guardado los datos porque no son válidos.")