from clases.prestamo import Prestamo
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from conexion_bd import ConexionBD


class GestionarPrestamo:
    def crear_prestamo(self) -> Prestamo:
        nie: str = ""
        nombre: str = ""
        apellidos: str = ""
        tramo: str = ""
        bilingue_str: str = ""
        bilingue: bool = False

        isbn: str = ""
        titulo: str = ""
        autor: str = ""
        ejemplares_str: str = ""
        editorial: str = ""
        materia: str = ""
        curso_nombre: str = ""
        ejemplares:int = 0

        nivel : str = ""

        fecha_entrega: str = ""
        estado: str = ""
        fecha_devolucion: str = ""

        nie = input("Introduce el NIE del alumno: ").strip().upper()
        nombre = input("Introduce el nombre del alumno: ").strip()
        apellidos = input("Introduce los apellidos del alumno: ").strip()
        tramo = input("Introduce el tramo: ").strip().upper()
        bilingue_str = input("¿Es bilingüe? (s/n): ").strip().lower()
        bilingue = True if bilingue_str == "s" else False

        alumno = Alumno(nie, nombre, apellidos, tramo, bilingue)

        isbn = input("Introduce el ISBN del libro: ").strip()
        titulo = input("Introduce el título del libro: ").strip()
        autor = input("Introduce el autor del libro: ").strip()
        ejemplares_str = input("Introduce los ejemplares del libro: ").strip()
        editorial = input("Introduce la editorial: ").strip()
        materia = input("Introduce la materia: ").strip()
        curso_nombre = input("Introduce el curso del libro: ").strip()

        try:
            ejemplares = int(ejemplares_str.replace(",", ""))
        except ValueError:
            print("Los ejemplares deben ser un número entero")
            return None

        libro = Libro(isbn, titulo, autor, ejemplares, editorial, materia, curso_nombre)

        nivel = input("Introduce el nivel del curso: ").strip()

        curso = Curso(curso_nombre, nivel)

        fecha_entrega = input("Introduce la fecha de entrega (AAAA-MM-DD): ").strip()
        estado = input("Introduce el estado del préstamo (P = Prestado, D = Devuelto): ").strip().upper()

        if estado == "D":
            fecha_devolucion = input("Introduce la fecha de devolución (AAAA-MM-DD): ").strip()

        prestamo = Prestamo(alumno, libro, curso, fecha_entrega, estado, fecha_devolucion)

        if prestamo.validar_datos_prestamo():
            print("El préstamo se ha creado correctamente.")
            return prestamo
        else:
            print("No se ha podido crear el préstamo.")
            return None


    def modificar_prestamo(self, prestamo: Prestamo) -> None:
        nuevo_curso: str = ""
        nueva_fecha_devolucion: str = ""
        nuevo_estado: str = ""

        curso_final: Curso = prestamo.curso
        fecha_devolucion_final: str = prestamo.fecha_devolucion
        estado_final: str = prestamo.estado

        nuevo_curso = input("Introduce el nuevo curso / Dejar vacío si no se quiere modificar: ").strip()
        nueva_fecha_devolucion = input("Introduce la fecha de devolución (AAAA-MM-DD) / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_estado = input("Introduce el estado (P = Prestado, D = Devuelto) / Dejar vacío si no se quiere modificar: ").strip().upper()

        if nuevo_curso != "":
            curso_final = Curso(nuevo_curso, "")
        if nueva_fecha_devolucion != "":
            fecha_devolucion_final = nueva_fecha_devolucion
        if nuevo_estado in ["P", "D"]:
            estado_final = nuevo_estado

        prestamo_temp: Prestamo = Prestamo(
            prestamo.alumno,
            prestamo.libro,
            curso_final,
            prestamo.fecha_entrega,
            estado_final,
            fecha_devolucion_final
        )

        if prestamo_temp.validar_datos_prestamo():
            prestamo.modificar_datos(curso_final, fecha_devolucion_final, estado_final)
            print("El préstamo se ha modificado correctamente.")

            conexion_bd = ConexionBD()
            conexion_bd.conectar_base_de_datos()

            update_prestamo = ("UPDATE alumnoscrusoslibros SET curso = '" + curso_final.curso +
        "', fecha_devolucion = '" + fecha_devolucion_final + "', estado = '" + estado_final +
        "' WHERE nie = '" + prestamo.alumno.nie + "' AND isbn = '" + prestamo.libro.isbn + "'")

        try:
            conexion_bd.ejecutar_consulta(update_prestamo)
            print("Los datos del préstamo se han actualziado en la base de datos")
        except:
            print("No se ha podido actualizar el préstamo en la base de datos")

        conexion_bd.cerrar()
