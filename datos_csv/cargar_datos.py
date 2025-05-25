import csv
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from clases.materia import Materia
from clases.prestamo import Prestamo
from conexion_bd import ConexionBD

def cargar_alumnos_desde_csv(ruta):
    alumnos = []
    conexion_bd = ConexionBD()
    conexion_bd.conectar_base_de_datos()
    conexion_bd.ejecutar_consulta("DELETE FROM alumnos")
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            alumno = Alumno(fila[0], fila[1], fila[2], fila[3], fila[4].lower() == 'true')
            alumnos.append(alumno)
            consulta = ("INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES ('" + alumno.nie + "', '" + alumno.nombre + "', '" + alumno.apellidos + "', '" + alumno.tramo + "', " + str(1 if alumno.bilingue else 0) + ")")
            conexion_bd.ejecutar_consulta(consulta)
    conexion_bd.cerrar()
    return alumnos

def cargar_libros_desde_csv(ruta):
    libros = []
    conexion_bd = ConexionBD()
    conexion_bd.conectar_base_de_datos()
    conexion_bd.ejecutar_consulta("DELETE FROM libros")
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            libro = Libro(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]), fila[5])
            libros.append(libro)
            consulta = ("INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) "
                        "VALUES ('" + libro.isbn + "', '" + libro.titulo + "', '" + libro.autor + "', " +
                        str(libro.ejemplares) + ", " + str(libro.materia) + ", '" + libro.curso + "')")
            conexion_bd.ejecutar_consulta(consulta)
    conexion_bd.cerrar()
    return libros




def cargar_cursos_desde_csv(ruta):
    cursos = []
    conexion_bd = ConexionBD()
    conexion_bd.conectar_base_de_datos()
    conexion_bd.ejecutar_consulta("DELETE FROM cursos")
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            curso = Curso(fila[0], fila[1])
            cursos.append(curso)
            consulta = ("INSERT INTO cursos (curso, nivel) VALUES ('" + curso.nombre + "', '" + curso.nivel + "')")
            conexion_bd.ejecutar_consulta(consulta)
    conexion_bd.cerrar()
    return cursos

def cargar_materias_desde_csv(ruta):
    materias = []
    conexion_bd = ConexionBD()
    conexion_bd.conectar_base_de_datos()
    conexion_bd.ejecutar_consulta("DELETE FROM materias")
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            materia = Materia(int(fila[0]), fila[1], fila[2])
            materias.append(materia)
            consulta = ("INSERT INTO materias (id, nombre, departamento) VALUES (" + str(materia.id) + ", '" + materia.nombre + "', '" + materia.departamento + "')")
            conexion_bd.ejecutar_consulta(consulta)
    conexion_bd.cerrar()
    return materias

def cargar_prestamos_desde_csv(ruta, alumnos, libros, cursos):
    prestamos = []
    conexion_bd = ConexionBD()
    conexion_bd.conectar_base_de_datos()
    conexion_bd.ejecutar_consulta("DELETE FROM alumnoscrusoslibros")
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            prestamo = Prestamo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            prestamos.append(prestamo)
            consulta = ("INSERT INTO alumnoscrusoslibros (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES ('" + prestamo.nie_alumno + "', '" + prestamo.curso + "', '" + prestamo.isbn_libro + "', '" + prestamo.fecha_entrega + "', '" + prestamo.fecha_devolucion + "', '" + prestamo.estado + "')")
            conexion_bd.ejecutar_consulta(consulta)
    conexion_bd.cerrar()
    return prestamos


