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
            consulta = "SELECT * FROM cursos WHERE curso = '" + curso_nombre + "'"
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
            except Exception as error:
                print("No se ha podido guardar el préstamo en la base de datos:", error)
        else:
            print("No se ha podido crear el préstamo: datos inválidos.")

        conexion_bd.cerrar()
        return prestamo

    def buscar_prestamo_por_nie_isbn(self, nie, isbn) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnoscursoslibros WHERE nie = '" + nie + "' AND isbn = '" + isbn + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("NIE:", fila[0], "ISBN:", fila[2], "Curso:", fila[1], "Fecha entrega:", fila[3], "Estado:", fila[5], "Fecha devolución:", fila[4])
        else:
            print("Préstamo no encontrado")
        conexion_bd.cerrar()

    def buscar_prestamos_por_estado(self, estado) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnoscursoslibros WHERE estado = '" + estado + "'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("NIE:", fila[0], "ISBN:", fila[2], "Curso:", fila[1], "Fecha entrega:", fila[3], "Estado:", fila[5], "Fecha devolución:", fila[4])
        else:
            print("No se encontraron préstamos")
        conexion_bd.cerrar()

    def listar_todos(self) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnoscursoslibros"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("NIE:", fila[0], "ISBN:", fila[2], "Curso:", fila[1], "Fecha entrega:", fila[3], "Estado:", fila[5], "Fecha devolución:", fila[4])
        else:
            print("No hay préstamos registrados")
        conexion_bd.cerrar()

    def modificar_prestamo(self, nie, isbn) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnoscursoslibros WHERE nie = '" + nie + "' AND isbn = '" + isbn + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("NIE:", fila[0], "ISBN:", fila[2], "Curso:", fila[1], "Fecha entrega:", fila[3], "Estado:", fila[5], "Fecha devolución:", fila[4])
            curso_final = fila[1]
            fecha_entrega_final = fila[3]
            estado_final = fila[5]
            fecha_devolucion_final = fila[4]

            nuevo_curso = input("Nuevo curso / Dejar vacío si no se modifica: ").strip()
            if nuevo_curso != "":
                curso_final = nuevo_curso

            nuevo_fecha_entrega = input("Nueva fecha de entrega (YYYY-MM-DD) / Dejar vacío si no se modifica: ").strip()
            if nuevo_fecha_entrega != "":
                fecha_entrega_final = nuevo_fecha_entrega

            nuevo_estado = input("Nuevo estado (P/D) / Dejar vacío si no se modifica: ").strip().upper()
            if nuevo_estado in ["P", "D"]:
                estado_final = nuevo_estado

            nuevo_fecha_devolucion = input("Nueva fecha de devolución (YYYY-MM-DD) / Dejar vacío si no se modifica: ").strip()
            if nuevo_fecha_devolucion != "":
                fecha_devolucion_final = nuevo_fecha_devolucion

            consulta_update = ("UPDATE alumnoscursoslibros SET curso = '" + curso_final + "', fecha_entrega = '" + fecha_entrega_final + "', estado = '" + estado_final + "', fecha_devolucion = '" + fecha_devolucion_final + "' WHERE nie = '" + nie + "' AND isbn = '" + isbn + "'")

            try:
                conexion_bd.ejecutar_consulta(consulta_update)
                print("El préstamo se ha modificado correctamente.")
            except:
                print("Error al modificar el préstamo en la base de datos.")
        else:
            print("Préstamo no encontrado")
        conexion_bd.cerrar()

    def generar_contrato_prestamo(self, nie, isbn):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnoscursoslibros WHERE nie = '" + nie + "' AND isbn = '" + isbn + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            nombre_archivo = "contrato_" + nie + "_" + isbn + ".txt"
            with open(nombre_archivo, "w", encoding='utf-8') as archivo:
                archivo.write("CONTRATO DE PRÉSTAMO\n")
                archivo.write("---------------------\n")
                archivo.write("NIE del alumno: " + fila[0] + "\n")
                archivo.write("ISBN del libro: " + fila[2] + "\n")
                archivo.write("Curso: " + fila[1] + "\n")
                archivo.write("Fecha de entrega: " + str(fila[3]) + "\n")
                archivo.write("Estado: " + fila[5] + "\n")
                archivo.write("Fecha de devolución: " + str(fila[4]) + "\n")
                archivo.write("\nFirma: __________________\n")
            print("El contrato se ha generado correctamente en el archivo:", nombre_archivo)
        else:
            print("Préstamo no encontrado")
        conexion_bd.cerrar()