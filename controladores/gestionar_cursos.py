from clases import curso
from conexion_bd import ConexionBD
from clases.curso import Curso

class GestionarCurso:
    def crear_curso(self) -> Curso:
        n_curso: str = ""
        nivel:str = ""

        curso = input("Introduce el nombre del curso (Ej: 1ESO, 2ESO, 1BACH, 2BACH): ").strip().upper()
        nivel = input("Introduce el nivel académico (Ej: ESO, Bachillerato, FP): ").strip().capitalize()

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        consulta = "SELECT * FROM cursos WHERE curso = '" + curso + "'"
        datos_curso = conexion_bd.obtener_datos(consulta)

        if len(datos_curso) == 0:
            curso_objeto = Curso(curso, nivel)
            insertar = "INSERT INTO cursos (curso, nivel) VALUES ('" + curso + "', '" + nivel + "')"
            try:
                conexion_bd.ejecutar_consulta(insertar)
                print("El curso se ha guardado correctamente.")
            except:
                print("No se pudo crear el curso.")
                conexion_bd.cerrar()
                return None
        else:
            print("El curso ya existe.")
            conexion_bd.cerrar()
            return None

        conexion_bd.cerrar()
        return curso_objeto

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
