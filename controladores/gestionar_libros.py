from clases.libro import Libro
from conexion_bd import ConexionBD

class GestionarLibro:
    def crear_libro(self) -> Libro:
        isbn: str = ""
        titulo: str = ""
        editorial: str = ""
        autor : str = ""
        ejemplares : str = ""
        materia: str = ""
        curso: str = ""

        isbn = input("Introduce el ISBN del libro (13 dígitos): ").strip()
        titulo = input("Introduce el título del libro: ").strip()
        autor = input("Introduce el autor del libro: ").strip()
        ejemplares = input("Introduce el ejemplar del libro: ").strip()
        editorial = input("Introduce la editorial: ").strip()
        materia = input("Introduce la materia: ").strip()
        curso = input("Introduce el curso: ").strip()

        libro: Libro = Libro(isbn, titulo, autor, ejemplares, editorial, materia, curso)

        if libro.validar_datos_libro():
            conexion_bd = ConexionBD()
            conexion_bd.conectar_base_de_datos()

            ejemplares = int(ejemplares.replace( " ", ""))

            add_libro = ("INSERT INTO libros (isbn, titulo, autor, ejemplares, editorial, materia, curso) " ""
                         "VALUES ('" + libro.isbn + "', '" + libro.titulo + "', '" + libro.autor + "', '"
                         + libro.ejemplares +  "', '" + libro.editorial + "', '" + libro.materia + "', " + libro.curso + ")")

            print("El libro se ha creado correctamente.", add_libro)

            try:
                conexion_bd.ejecutar_consulta(add_libro)
                print("El libro se ha creado correctamente.")
            except:
                print("No se ha podido crear el libro en la base de datos.")

            conexion_bd.cerrar()
            return libro

        else:
            print("No se ha podido crear el libro. Revisa los datos introducidos.")
            return None


    def modificar_libro(self, libro: Libro) -> None:
        nuevo_titulo: str = ""
        nuevo_autor: str = ""
        nuevo_ejemplares: str = ""
        nuevo_editorial: str = ""
        nuevo_materia: str = ""
        nuevo_curso: str = ""

        titulo_final: str = ""
        autor_final: str = ""
        ejemplares_final: str = ""
        editorial_final: str = ""
        materia_final: str = ""
        curso_final: str = ""

        nuevo_titulo = input("Introduce el nuevo título / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_autor = input("Introduce el nuevo autor / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_ejemplares = input("Introduce el nuevo número de ejemplares / Dejar vacío si no se quiere modificar:").strip()
        nuevo_editorial = input("Introduce la nueva editorial / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_materia = input("Introduce la nueva materia / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_curso = input("Introduce el nuevo curso / Dejar vacío si no se quiere modificar: ").strip()

        titulo_final = libro.titulo if nuevo_titulo == "" else nuevo_titulo
        autor_final = libro.autor if nuevo_autor == "" else nuevo_autor
        ejemplares_final = libro.ejemplares if nuevo_ejemplares == "" else nuevo_ejemplares
        editorial_final = libro.editorial if nuevo_editorial == "" else nuevo_editorial
        materia_final = libro.materia if nuevo_materia == "" else nuevo_materia
        curso_final = libro.curso if nuevo_curso == "" else nuevo_curso

        libro_temporal: Libro = Libro(libro.isbn, titulo_final, autor_final, ejemplares_final, editorial_final, materia_final, curso_final)

        if libro_temporal.validar_datos_libro():
            libro.modificar_datos(titulo_final, autor_final, ejemplares_final, materia_final, curso_final)
            print("El libro se ha modificado correctamente.")
        else:
            print("No se han guardado los datos porque no son válidos.")