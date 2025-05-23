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

        nie = input("Introduce el NIE del alumno: ").strip().upper()
        consulta_alumno = "SELECT * FROM alumnos WHERE nie = '" + nie + "'"
        datos_alumno = conexion_bd.obtener_datos(consulta_alumno)

        if len(datos_alumno) == 0:
            print("El alumno no existe ¿Quieres crearlo?")
            respuesta = input("s/n: ").strip().lower()
            if respuesta == "s":
                alumno = gestion_alumnos.crear_alumno()
            else:
                print("No se puede continuar sin un alumno.")
                conexion_bd.cerrar()
                return None
        else:
            datos = datos_alumno[0]
            bilingue = True if datos[4] == 1 else False
            alumno = Alumno(datos[0], datos[1], datos[2], datos[3], bilingue)

        isbn = input("Introduce el ISBN del libro: ").strip()
        consulta_libro = "SELECT * FROM libros WHERE isbn = '" + isbn + "'"
        datos_libro = conexion_bd.obtener_datos(consulta_libro)

        if len(datos_libro) == 0:
            print("El libro no existe ¿Quieres crearlo?")
            respuesta = input("s/n: ").strip().lower()
            if respuesta == "s":
                libro = gestion_libros.crear_libro()
            else:
                print("No se puede continuar sin un libro.")
                conexion_bd.cerrar()
                return None
        else:
            datos = datos_libro[0]
            libro = Libro(datos[0], datos[1], datos[2], datos[3], "", datos[4], datos[5])

        curso_nombre = input("Introduce el curso del alumno: ").strip()
        consulta_curso = "SELECT * FROM cursos WHERE nombre = '" + curso_nombre + "'"
        datos_curso = conexion_bd.obtener_datos(consulta_curso)

        if len(datos_curso) == 0:
            print("El curso no existe ¿Quieres crearlo?")
            respuesta = input("s/n: ").strip().lower()
            if respuesta == "s":
                curso = gestion_curso.crear_curso()
            else:
                print("No se puede continuar sin un curso.")
                conexion_bd.cerrar()
                return None
        else:
            datos = datos_curso[0]
            curso = Curso(datos[0], datos[1])

        fecha_entrega = input("Introduce la fecha de (AAAA-MM-DD): ").strip()
        estado = input("Introduce el estado del alumno (P = prestado o D = devuelto): ").strip()

        if estado == "D":
            fecha_devolucion = input("Introduce la fecha de devolución (AAAA-MM-DD): ").strip()

        prestamo = Prestamo(alumno, libro, curso, fecha_entrega, estado, fecha_devolucion)

        if prestamo.validar_datos_prestamo():
            insert_prestamo = ("INSERT INTO alumnoscrusoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES ('"
                + alumno.nie + "', '" + curso.curso + "', '" + libro.isbn + "', '"
                + fecha_entrega + "', '" + fecha_devolucion + "', '" + estado + "')")
            try:
                conexion_bd.ejecutar_consulta(insert_prestamo)
                print("El préstamo se ha guardado correctamente.")
            except:
                print("No se ha podido guardar el préstamo en la base de datos.")

            conexion_bd.cerrar()
            return prestamo

        else:
            print("No se ha podido crear el préstamo.")
            conexion_bd.cerrar()
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
            conexion_bd = ConexionBD()
            conexion_bd.conectar_base_de_datos()

            consulta = "SELECT curso FROM cursos WHERE curso = '" + nuevo_curso + "'"
            resultados = conexion_bd.obtener_datos(consulta)

            if len(resultados) == 0:
                print("El curso no existe ¿Quieres crearlo?")
                respuesta = input("s/n: ").strip().lower()
                if respuesta == "s":
                    nivel = input("Introduce el nivel del curso: ")
                    insertar = "INSERT INTO cursos (curso, nivel) VALUES ('" + nuevo_curso + "', '" + nivel + "')"
                    try:
                        conexion_bd.ejecutar_consulta(insertar)
                        print("El curso se ha guardado correctamente.")
                    except:
                        print("No se puedo crear el curso")
                        conexion_bd.cerrar()
                        return

                else:
                    print("No se ha podido modficar el préstamo.")
                    conexion_bd.cerrar()
                    return

            conexion_bd.cerrar()
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

            update_prestamo = ("UPDATE alumnoscursoslibros SET curso = '" + curso_final.curso +
            "', fecha_devolucion = '" + fecha_devolucion_final + "', estado = '" + estado_final +
            "' WHERE nie = '" + prestamo.alumno.nie + "' AND isbn = '" + prestamo.libro.isbn + "'")

            try:
                conexion_bd.ejecutar_consulta(update_prestamo)
                print("Los datos del préstamo se han actualizado en la base de datos")
            except:
                print("No se ha podido actualizar el préstamo en la base de datos")
            conexion_bd.cerrar()
        else:
            print("Los datos no se han guardado porque no son válidos")

