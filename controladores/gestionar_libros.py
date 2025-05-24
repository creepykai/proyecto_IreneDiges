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

        titulo_final: str = libro.titulo
        autor_final: str = libro.autor
        ejemplares_final: int = libro.ejemplares
        editorial_final: str = libro.editorial
        materia_final: str = libro.materia
        curso_final: str = libro.curso

        nuevo_titulo = input("Introduce el nuevo título / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_titulo != "":
            titulo_final = nuevo_titulo

        nuevo_autor = input("Introduce el nuevo autor / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_autor != "":
            autor_final = nuevo_autor

        nuevo_ejemplares_str = input(
            "Introduce el nuevo número de ejemplares / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_ejemplares_str != "":
            try:
                ejemplares_final = int(nuevo_ejemplares_str)
            except ValueError:
                print("Los ejemplares deben ser un número entero. Se mantiene el valor anterior.")

        nuevo_editorial = input("Introduce la nueva editorial / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_editorial != "":
            editorial_final = nuevo_editorial

        nuevo_materia = input("Introduce la nueva materia / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_materia != "":
            materia_final = nuevo_materia

        nuevo_curso = input("Introduce el nuevo curso / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_curso != "":
            curso_final = nuevo_curso

        try:
            libro_temp = Libro(libro.isbn, titulo_final, autor_final, ejemplares_final, editorial_final,
                               materia_final, curso_final)
        except ValueError as e:
            print("Error al modificar el libro:", e)
            return

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update_libro = ("UPDATE libros SET titulo = '" + titulo_final + "', autor = '" + autor_final +
                "', ejemplares = " + str(ejemplares_final) + ", editorial = '" + editorial_final +
                "', materia = '" + materia_final + "', curso = '" + curso_final +
                "' WHERE isbn = '" + libro.isbn + "'")

        try:
            conexion_bd.ejecutar_consulta(update_libro)
            print("El libro se ha modificado correctamente.")
        except:
            print("Error al modificar el libro en la base de datos.")
        finally:
            conexion_bd.cerrar()
