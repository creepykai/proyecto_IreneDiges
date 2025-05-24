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


    def modificar_curso(self, curso_objeto: Curso) -> None:
        nombre_curso: str = ""
        nuevo_nivel: str = ""

        nombre_curso = input("Introduce el nombre del curso que deseas modificar")

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        consulta = "SELECT * FROM cursos WHERE curso = '" + nombre_curso + "'"
        datos_curso = conexion_bd.obtener_datos(consulta)

        if len(datos_curso) == 0:
            print("El curso no existe.")
            conexion_bd.cerrar()
            return None

        nuevo_nivel = input("Introduce el nivel que deseas modificar (Ej: ESO, Bachillerato, FP)")

        actualizar = "UPDATE cursos SET nivel = '" + nuevo_nivel + "' WHERE curso = '" + nombre_curso + "'"

        try:
            conexion_bd.ejecutar_consulta(actualizar)
            print("El curso se ha modificado correctamente.")
        except:
            print("No se ha podido modificar el curso en la base de datos.")

        conexion_bd.cerrar()
