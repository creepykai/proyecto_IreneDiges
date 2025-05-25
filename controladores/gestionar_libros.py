from clases.libro import Libro
from conexion_bd import ConexionBD

class GestionarLibro:
    def crear_libro(self) -> Libro:
        isbn: str = ""
        titulo: str = ""
        autor: str = ""
        ejemplares_str: str = ""
        ejemplares: int = 0
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
            materia = input("Introduce la materia (id): ").strip()
            if materia != "":
                break
            print("La materia no puede estar vacía.")

        while True:
            curso = input("Introduce el curso (id) (1ESO, 2ESO, etc. -> sin º): ").strip()
            if curso != "":
                break
            print("El curso no puede estar vacío.")

        try:
            libro = Libro(isbn, titulo, autor, ejemplares, materia, curso)
        except ValueError as error:
            print("Error al crear el libro:", error)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        add_libro = ("INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) "
                     "VALUES ('" + libro.isbn + "', '" + libro.titulo + "', '" + libro.autor + "', " +
                     str(libro.ejemplares) + ", '" + libro.materia + "', '" + libro.curso + "')")

        try:
            conexion_bd.ejecutar_consulta(add_libro)
            print("El libro se ha creado correctamente.")
        except ValueError as error:
            print("No se ha podido crear el libro en la base de datos. Error:", error)

        conexion_bd.cerrar()
        return libro

    def buscar_libro_por_isbn(self, isbn) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM libros WHERE isbn = '" + isbn + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("ISBN:", fila[0], "Título:", fila[1], "Autor:", fila[2], "Ejemplares:", fila[3], "Materia:", fila[4], "Curso:", fila[5])
        else:
            print("Libro no encontrado")
        conexion_bd.cerrar()

    def buscar_libros_por_autor(self, autor):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM libros WHERE autor LIKE '%" + autor + "%'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("ISBN:", fila[0], "Título:", fila[1], "Autor:", fila[2], "Ejemplares:", fila[3], "Materia:", fila[4], "Curso:", fila[5])
        else:
            print("No se encontraron libros")
        conexion_bd.cerrar()

    def buscar_libros_por_materia(self, materia) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM libros WHERE id_materia LIKE '%" + materia + "%'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("ISBN:", fila[0], "Título:", fila[1], "Autor:", fila[2], "Ejemplares:", fila[3], "Materia:", fila[4], "Curso:", fila[5])
        else:
            print("No se encontraron libros")
        conexion_bd.cerrar()

    def listar_todos(self) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM libros"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("ISBN:", fila[0], "Título:", fila[1], "Autor:", fila[2], "Ejemplares:", fila[3], "Materia:", fila[4], "Curso:", fila[5])
        else:
            print("No hay libros registrados")
        conexion_bd.cerrar()

    def modificar_libro(self, isbn) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM libros WHERE isbn = '" + isbn + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("ISBN:", fila[0], "Título:", fila[1], "Autor:", fila[2], "Ejemplares:", fila[3], "Materia:", fila[4], "Curso:", fila[5])
            titulo_final = fila[1]
            autor_final = fila[2]
            ejemplares_final = fila[3]
            materia_final = fila[4]
            curso_final = fila[5]

            nuevo_titulo = input("Nuevo título / Dejar vacío si no se modifica: ").strip()
            if nuevo_titulo != "":
                titulo_final = nuevo_titulo

            nuevo_autor = input("Nuevo autor / Dejar vacío si no se modifica: ").strip()
            if nuevo_autor != "":
                autor_final = nuevo_autor

            nuevo_ejemplares = input("Nuevo número de ejemplares / Dejar vacío si no se modifica: ").strip()
            if nuevo_ejemplares.isdigit():
                ejemplares_final = int(nuevo_ejemplares)

            nuevo_materia = input("Nueva materia / Dejar vacío si no se modifica: ").strip()
            if nuevo_materia != "":
                materia_final = nuevo_materia

            nuevo_curso = input("Nuevo curso / Dejar vacío si no se modifica: ").strip()
            if nuevo_curso != "":
                curso_final = nuevo_curso

            consulta_update = ("UPDATE libros SET titulo = '" + titulo_final + "', autor = '" + autor_final + "', numero_ejemplares = " + str(ejemplares_final) +
                               ", id_materia = '" + materia_final + "', id_curso = '" + curso_final + "' WHERE isbn = '" + isbn + "'")

            try:
                conexion_bd.ejecutar_consulta(consulta_update)
                print("El libro se ha modificado correctamente.")
            except:
                print("Error al modificar el libro en la base de datos.")
        else:
            print("Libro no encontrado")
        conexion_bd.cerrar()
