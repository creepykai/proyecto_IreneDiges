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
        except ValueError as error:
            print("Error al crear el curso:", error)
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

    def buscar_curso_por_nombre(self, nombre):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM cursos WHERE nombre LIKE '" + nombre + "'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("Nombre:", fila[0], "Nivel:", fila[1])
        else:
            print("No se encontraron cursos")
        conexion_bd.cerrar()

    def buscar_cursos_por_nivel(self, nivel):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM cursos WHERE nivel LIKE '" + nivel + "'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("Nombre:", fila[0], "Nivel:", fila[1])
        else:
            print("No se encontraron cursos")
        conexion_bd.cerrar()

    def listar_todos(self):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM cursos"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("Nombre:", fila[0], "Nivel:", fila[1])
        else:
            print("No hay cursos registrados")
        conexion_bd.cerrar()

    def modificar_curso(self, nombre):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM cursos WHERE nombre = '" + nombre + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("Nombre:", fila[0], "Nivel:", fila[1])
            nombre_final = fila[0]
            nivel_final = fila[1]

            nuevo_nombre = input("Nuevo nombre / Dejar vacío si no se modifica: ").strip()
            if nuevo_nombre != "":
                nombre_final = nuevo_nombre

            nuevo_nivel = input("Nuevo nivel / Dejar vacío si no se modifica: ").strip()
            if nuevo_nivel != "":
                nivel_final = nuevo_nivel

            consulta_update = "UPDATE cursos SET nombre = '" + nombre_final + "', nivel = '" + nivel_final + "' WHERE nombre = '" + nombre + "'"

            try:
                conexion_bd.ejecutar_consulta(consulta_update)
                print("El curso se ha modificado correctamente.")
            except:
                print("Error al modificar el curso en la base de datos.")
        else:
            print("Curso no encontrado")
        conexion_bd.cerrar()

