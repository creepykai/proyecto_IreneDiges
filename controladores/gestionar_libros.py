from clases.libro import Libro
from conexion_bd import ConexionBD

class GestionarLibro:
    def crear_libro(self) -> Libro:
        isbn: str = ""
        titulo: str = ""
        editorial: str = ""
        autor : str = ""
        ejemplares_str : str = ""
        ejemplares : int = 0
        materia: str = ""
        curso: str = ""

        while True:
            isbn = input("Introduce el ISBN del libro (13 dígitos): ").strip()
            if len(isbn) == 13 and isbn.isdigit():
                break
            print("El ISBN debe tener exactamente 13 dígitos numéricos.")

        while True:
            titulo = input("Introduce el título del libro: ").strip()
            if titulo != "" and any(c.isalpha() for c in titulo):
                break
            print("El título no puede estar vacío y debe tener letras.")

        while True:
            autor = input("Introduce el autor del libro: ").strip()
            if autor != "" and any(c.isalpha() for c in autor):
                break
            print("El autor no puede estar vacío y debe tener letras.")

        while True:
            ejemplares_str = input("Introduce la cantidad de ejemplares: ").strip()
            if ejemplares_str.isdigit() and int(ejemplares_str) > 0:
                ejemplares = int(ejemplares_str)
                break
            print("Los ejemplares deben ser un número entero mayor que cero.")

        while True:
            editorial = input("Introduce la editorial: ").strip()
            if editorial != "" and any(c.isalpha() for c in editorial):
                break
            print("La editorial no puede estar vacía y debe tener letras.")

        while True:
            materia = input("Introduce la materia: ").strip()
            if materia != "" and any(c.isalpha() for c in materia):
                break
            print("La materia no puede estar vacía y debe tener letras.")

        while True:
            curso = input("Introduce el curso: ").strip()
            if curso != "" and any(c.isalpha() for c in curso):
                break
            print("El curso no puede estar vacío y debe tener letras.")

        try:
            libro = Libro(isbn, titulo, autor, ejemplares, editorial, materia, curso)
        except ValueError as e:
            print("Error al crear el libro:", e)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        add_libro = ("INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) "
                     "VALUES ('" + libro.isbn + "', '" + libro.titulo + "', '" + libro.autor + "', " +
                     str(libro.ejemplares) + ", '" + libro.materia + "', '" + libro.curso + "')")

        try:
            conexion_bd.ejecutar_consulta(add_libro)
            print("El libro se ha creado correctamente.")
        except:
            print("No se ha podido crear el libro en la base de datos.")

        conexion_bd.cerrar()
        return libro

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

        if nuevo_ejemplares != "":
            try:
                ejemplares_final = int(nuevo_ejemplares)
            except ValueError:
                print("Error: el número de ejemplares debe ser un número entero.")
                return

        try:
            libro_temporal: Libro = Libro(libro.isbn, titulo_final, autor_final, ejemplares_final, editorial_final, materia_final, curso_final)
        except ValueError as error:
            print("Error al modificar el libro:", error)
            return

        libro.modificar_datos(titulo_final, autor_final, ejemplares_final, materia_final, curso_final)

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        consulta: str = (
                "UPDATE libros SET titulo = '" + libro.titulo +
                "', autor = '" + libro.autor +
                "', numero_ejemplares = " + str(libro.ejemplares) +
                ", editorial = '" + libro.editorial +
                "', id_materia = '" + libro.materia +
                "', id_curso = '" + libro.curso +
                "' WHERE isbn = '" + libro.isbn + "'"
        )

        try:
            conexion_bd.ejecutar_consulta(consulta)
            print("El libro se ha modificado correctamente.")
        except:
            print("No se ha podido modificar el libro en la base de datos.")

        conexion_bd.cerrar()
