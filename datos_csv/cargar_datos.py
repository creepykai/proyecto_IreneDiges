import csv
from clases.libro import Libro
from clases.materia import Materia
from clases.curso import Curso
from conexion_bd import ConexionBD

def cargar_materias_desde_csv(ruta_csv) -> None:
    conexion = ConexionBD()
    conexion.conectar_base_de_datos()
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                try:
                    materia = Materia(int(fila[0]), fila[1], fila[2])
                    consulta = ("INSERT INTO materias (id, nombre, departamento) VALUES ('" + str(materia.id) + "', '" + materia.materia + "', '" + materia.departamento + "')")
                    conexion.ejecutar_consulta(consulta)
                    print("Materia añadida correctamente:", materia)
                except Exception as error:
                    print("Error al añadir materia:", error)
    except Exception as error:
        print("Error al abrir el archivo de materias:", error)
    finally:
        conexion.cerrar()

def cargar_cursos_desde_csv(ruta_csv) -> None:
    conexion = ConexionBD()
    conexion.conectar_base_de_datos()
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                try:
                    curso = Curso(fila[0], fila[1])
                    consulta = ("INSERT INTO cursos (curso, nivel) VALUES ('" + curso.curso + "', '" + curso.nivel + "')")
                    conexion.ejecutar_consulta(consulta)
                    print("Curso añadido correctamente:", curso)
                except Exception as error:
                    print("Error al añadir curso:", error)
    except Exception as error:
        print("Error al abrir el archivo de cursos:", error)
    finally:
        conexion.cerrar()

def cargar_libros_desde_csv(ruta_csv) -> None:
    conexion = ConexionBD()
    conexion.conectar_base_de_datos()
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                try:
                    libro = Libro(fila[0], fila[1], fila[2], int(fila[3]), fila[4], fila[5])
                    curso_existente = conexion.obtener_datos("SELECT curso FROM cursos WHERE curso = '" + libro.curso + "'")
                    if not curso_existente:
                        print("Curso no encontrado en base de datos, libro saltado:", libro.curso)
                        continue
                    materia_existente = conexion.obtener_datos("SELECT id FROM materias WHERE id = '" + libro.materia + "'")
                    if not materia_existente:
                        print("Materia no encontrada en base de datos, libro saltado:", libro.materia)
                        continue
                    consulta = ("INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) "
                                "VALUES ('" + libro.isbn + "', '" + libro.titulo + "', '" + libro.autor + "', " + str(libro.ejemplares) + ", '" + libro.materia + "', '" + libro.curso + "')")
                    conexion.ejecutar_consulta(consulta)
                    print("Libro añadido correctamente:", libro)
                except Exception as error:
                    print("Error al añadir libro:", error)
    except Exception as error:
        print("Error al abrir el archivo de libros:", error)
    finally:
        conexion.cerrar()

def cargar_alumnos_desde_csv(ruta_csv) -> None:
    conexion = ConexionBD()
    conexion.conectar_base_de_datos()
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                try:
                    nie = fila[0]
                    nombre = fila[1]
                    apellidos = fila[2]
                    tramo = fila[3]
                    bilingue_str = fila[4].strip().lower()
                    if bilingue_str == 'true':
                        bilingue = 1
                    else:
                        bilingue = 0
                    consulta = ("INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) "
                                "VALUES ('" + nie + "', '" + nombre + "', '" + apellidos + "', '" + tramo + "', " + str(bilingue) + ")")
                    conexion.ejecutar_consulta(consulta)
                    print("Alumno añadido correctamente:", nie, nombre, apellidos)
                except Exception as error:
                    print("Error al añadir alumno:", error)
    except Exception as error:
        print("Error al abrir el archivo de alumnos:", error)
    finally:
        conexion.cerrar()

def cargar_prestamos_desde_csv(ruta_csv) -> None:
    conexion = ConexionBD()
    conexion.conectar_base_de_datos()
    try:
        with open(ruta_csv, newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo, delimiter=',')
            for fila in lector:
                try:
                    nie = fila[0].strip()
                    curso = fila[1].strip()
                    isbn = fila[2].strip()
                    fecha_prestamo = fila[3].strip()
                    fecha_devolucion = fila[4].strip()
                    estado = fila[5].strip().upper()

                    if estado not in ['P', 'D']:
                        print(f"Estado desconocido '{estado}' en fila, saltada: {fila}")
                        continue

                    existente = conexion.obtener_datos(
                        "SELECT * FROM alumnoscursoslibros WHERE nie = '" + nie + "' AND isbn = '" + isbn + "' AND fecha_entrega = '" + fecha_prestamo + "'")
                    if existente:
                        print(f"Préstamo ya existente, saltado: NIE {nie}, ISBN {isbn}, Fecha {fecha_prestamo}")
                        continue

                    consulta = ("INSERT INTO alumnoscursoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) "
                                "VALUES ('" + nie + "', '" + curso + "', '" + isbn + "', '" + fecha_prestamo + "', '" + fecha_devolucion + "', '" + estado + "')")
                    conexion.ejecutar_consulta(consulta)
                    print("Préstamo añadido correctamente:", nie, isbn, estado)
                except Exception as error:
                    print("Error al añadir préstamo:", error)
    except Exception as error:
        print("Error al abrir el archivo de préstamos:", error)
    finally:
        conexion.cerrar()


