from clases import curso
from conexion_bd import ConexionBD
from clases.curso import Curso

class GestionarCurso:
    def crear_curso(self) -> Curso:
        n_curso: str = ""
        nivel:str = ""

        while True:
            nombre = input("Introduce el nombre del curso (ej. 1ESO, 2Bachillerato): ").strip()
            if nombre != "" and any(c.isalnum() for c in nombre):
                break
            print("El nombre del curso no puede estar vacío y debe tener letras o números.")

        while True:
            nivel = input("Introduce el nivel del curso (ej. ESO, Bachillerato): ").strip()
            if nivel != "" and any(c.isalpha() for c in nivel):
                break
            print("El nivel no puede estar vacío y debe tener letras.")

        try:
            curso = Curso(nombre, nivel)
        except ValueError as e:
            print("Error al crear el curso:", e)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        add_curso = ("INSERT INTO cursos (nombre, nivel) "
                     "VALUES ('" + curso.curso + "', '" + curso.nivel + "')")

        try:
            conexion_bd.ejecutar_consulta(add_curso)
            print("El curso se ha creado correctamente.")
        except Exception as error:
            print("No se ha podido crear el curso en la base de datos:", error)
        finally:
            conexion_bd.cerrar()

        return curso


    def modificar_curso(self, curso: Curso) -> None:
        nombre_curso: str = ""
        nuevo_nivel: str = ""
        nuevo_nombre: str = ""

        nombre_final: str = curso.curso
        nivel_final: str = curso.nivel

        nuevo_nombre = input("Introduce el nuevo nombre del curso / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_nombre != "":
            nombre_final = nuevo_nombre

        nuevo_nivel = input("Introduce el nuevo nivel del curso / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_nivel != "":
            nivel_final = nuevo_nivel

        try:
            curso_temporal = Curso(nombre_final, nivel_final)
        except ValueError as error:
            print("Error al modificar el curso:", error)
            return

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update_curso = ("UPDATE cursos SET nombre = '" + nombre_final + "', nivel = '" + nivel_final +
                "' WHERE nombre = '" + curso.curso + "'")

        try:
            conexion_bd.ejecutar_consulta(update_curso)
            print("El curso se ha modificado correctamente.")
        except:
            print("Error al modificar el curso en la base de datos.")
        finally:
            conexion_bd.cerrar()
