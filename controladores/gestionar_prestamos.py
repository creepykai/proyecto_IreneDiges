from conexion_bd import ConexionBD
from clases.prestamo import Prestamo
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from controladores.gestionar_alumnos import GestionarAlumnos
from controladores.gestionar_cursos import GestionarCurso
from controladores.gestionar_libros import GestionarLibro


class GestionarPrestamo:
    def crear_prestamo(self) -> Prestamo:
        nie: str = ""
        isbn: str = ""
        titulo: str = ""
        curso_nombre: str = ""
        fecha_entrega: str = ""
        estado: str = ""
        fecha_devolucion: str = ""
        alumno: Alumno = None
        libro: Libro = None
        curso: Curso = None

        gestion_alumnos = GestionarAlumnos()
        gestion_libros = GestionarLibro()
        gestion_curso = GestionarCurso()

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        while True:
            nie = input("Introduce el NIE del alumno: ").strip().upper()
            consulta = "SELECT * FROM alumnos WHERE nie = '" + nie + "'"
            datos_alumno = conexion_bd.obtener_datos(consulta)
            if datos_alumno:
                datos = datos_alumno[0]
                bilingue = True if datos[4] == 1 else False
                alumno = Alumno(datos[0], datos[1], datos[2], datos[3], bilingue)
                break
            print("El NIE no existe. Por favor, verifica los datos.")

        while True:
            isbn = input("Introduce el ISBN del libro: ").strip()
            consulta = "SELECT * FROM libros WHERE isbn = '" + isbn + "'"
            datos_libro = conexion_bd.obtener_datos(consulta)
            if datos_libro:
                datos = datos_libro[0]
                libro = Libro(datos[0], datos[1], datos[2], int(datos[3]), datos[4], datos[5], datos[6])
                break
            print("El ISBN no existe. Por favor, verifica los datos.")

        while True:
            curso_nombre = input("Introduce el curso del alumno: ").strip()
            consulta = "SELECT * FROM cursos WHERE nombre = '" + curso_nombre + "'"
            datos_curso = conexion_bd.obtener_datos(consulta)
            if datos_curso:
                datos = datos_curso[0]
                curso = Curso(datos[0], datos[1])
                break
            print("El curso no existe. Por favor, verifica los datos.")

        while True:
            fecha_entrega = input("Introduce la fecha de entrega (AAAA-MM-DD): ").strip()
            if Prestamo.validar_fecha(fecha_entrega, "fecha de entrega"):
                break
            print("La fecha no tiene el formato correcto.")

        while True:
            estado = input("Introduce el estado (P = Prestado, D = Devuelto): ").strip().upper()
            if estado in ["P", "D"]:
                break
            print("El estado debe ser 'P' o 'D'.")

        if estado == "D":
            while True:
                fecha_devolucion = input("Introduce la fecha de devolución (AAAA-MM-DD): ").strip()
                if Prestamo.validar_fecha(fecha_devolucion, "fecha de devolución"):
                    break
                print("La fecha no tiene el formato correcto.")

        prestamo = Prestamo(alumno, libro, curso, fecha_entrega, estado, fecha_devolucion)

        if prestamo.validar_datos_prestamo():
            insert_prestamo = ("INSERT INTO alumnoscursoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) "
                    "VALUES ('" + alumno.nie + "', '" + curso.curso + "', '" + libro.isbn + "', '" + fecha_entrega + "', '" + fecha_devolucion + "', '" + estado + "')")
            try:
                conexion_bd.ejecutar_consulta(insert_prestamo)
                print("El préstamo se ha guardado correctamente.")
            except Exception as e:
                print("No se ha podido guardar el préstamo en la base de datos:", e)
        else:
            print("No se ha podido crear el préstamo: datos inválidos.")

        conexion_bd.cerrar()
        return prestamo

    def modificar_prestamo(self, prestamo: Prestamo) -> None:
        nuevo_curso: str = ""
        nueva_fecha_devolucion: str = ""
        nuevo_estado: str = ""

        curso_final: Curso = prestamo.curso
        fecha_devolucion_final: str = prestamo.fecha_devolucion
        estado_final: str = prestamo.estado

        nuevo_curso = input("Introduce el nuevo curso / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_curso != "":
            curso_final = Curso(nuevo_curso, "")

        nueva_fecha_devolucion = input("Introduce la nueva fecha de devolución (AAAA-MM-DD) / Dejar vacío si no se quiere modificar: ").strip()

        if nueva_fecha_devolucion != "":
            fecha_devolucion_final = nueva_fecha_devolucion

        nuevo_estado = input(
            "Introduce el nuevo estado (P = Prestado, D = Devuelto) / Dejar vacío si no se quiere modificar: ").strip().upper()

        if nuevo_estado in ["P", "D"]:
            estado_final = nuevo_estado

        try:
            prestamo_temp = Prestamo(
                prestamo.alumno,
                prestamo.libro,
                curso_final,
                prestamo.fecha_entrega,
                estado_final,
                fecha_devolucion_final
            )
        except ValueError as e:
            print("Error al modificar el préstamo:", e)
            return

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update_prestamo = ("UPDATE alumnoscursoslibros SET curso = '" + curso_final.curso +"', fecha_devolucion = '" + fecha_devolucion_final +
                "', estado = '" + estado_final + "' WHERE nie = '" + prestamo.alumno.nie + "' AND isbn = '" + prestamo.libro.isbn + "'")

        try:
            conexion_bd.ejecutar_consulta(update_prestamo)
            print("El préstamo se ha modificado correctamente en la base de datos.")
        except:
            print("Error al modificar el préstamo en la base de datos.")
        finally:
            conexion_bd.cerrar()
