from conexion_bd import ConexionBD
from clases.materia import Materia

class GestionarMaterias:
    def crear_materia(self) -> Materia:
        id_str: str = ""
        materia_nombre: str = ""
        departamento: str = ""

        while True:
            id_str = input("Introduce el ID de la materia (número entero): ").strip()
            if id_str.isdigit() and int(id_str) > 0:
                id_materia = int(id_str)
                break
            print("El ID debe ser un número entero positivo.")

        while True:
            materia = input("Introduce el nombre de la materia: ").strip()
            if materia != "" and any(c.isalpha() for c in materia):
                break
            print("La materia no puede estar vacía y debe tener letras.")

        while True:
            departamento = input("Introduce el departamento: ").strip()
            if departamento != "" and any(c.isalpha() for c in departamento):
                break
            print("El departamento no puede estar vacío y debe tener letras.")

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        consulta = "SELECT * FROM materias WHERE nombre = '" + materia_nombre + "'"
        datos_materia = conexion_bd.obtener_datos(consulta)

        if len(datos_materia) > 0:
            print("La materia ya existe. No se puede duplicar.")
            conexion_bd.cerrar()
            return None

        try:
            materia: Materia = Materia(id_materia,materia_nombre, departamento)
        except ValueError as error:
            print("Error al crear la materia", error)
            return None



        insertar = ("INSERT INTO materias (id, materia, departamento) "
                "VALUES ('" + materia.id + "', '" + materia.materia + "', '" + materia.departamento + "')")

        try:
            conexion_bd.ejecutar_consulta(insertar)
            print("Materia creada con exito")
        except ValueError as error:
            print("No se ha podido guardar la materia en la BDD. Error: ", error)

        conexion_bd.cerrar()
        return materia

    def buscar_materia_por_id(self, id_materia):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM materias WHERE id = '" + id_materia + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("ID:", fila[0], "Nombre:", fila[1], "Departamento:", fila[2])
        else:
            print("Materia no encontrada")
        conexion_bd.cerrar()

    def buscar_materias_por_departamento(self, departamento):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM materias WHERE departamento LIKE '" + departamento + "'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("ID:", fila[0], "Nombre:", fila[1], "Departamento:", fila[2])
        else:
            print("No se encontraron materias")
        conexion_bd.cerrar()

    def listar_todos(self):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM materias"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("ID:", fila[0], "Nombre:", fila[1], "Departamento:", fila[2])
        else:
            print("No hay materias registradas")
        conexion_bd.cerrar()

    def modificar_materia(self, nombre) -> None:
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM materias WHERE nombre = '" + nombre + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("ID:", fila[0], "Nombre:", fila[1], "Departamento:", fila[2])
            nombre_final = fila[1]
            departamento_final = fila[2]

            nuevo_nombre = input("Nuevo nombre / Dejar vacío si no se modifica: ").strip()
            if nuevo_nombre != "":
                nombre_final = nuevo_nombre

            nuevo_departamento = input("Nuevo departamento / Dejar vacío si no se modifica: ").strip()
            if nuevo_departamento != "":
                departamento_final = nuevo_departamento

            consulta_update = "UPDATE materias SET nombre = '" + nombre_final + "', departamento = '" + departamento_final + "' WHERE nombre = '" + nombre + "'"

            try:
                conexion_bd.ejecutar_consulta(consulta_update)
                print("La materia se ha modificado correctamente.")
            except:
                print("Error al modificar la materia en la base de datos.")
        else:
            print("Materia no encontrada")
        conexion_bd.cerrar()
