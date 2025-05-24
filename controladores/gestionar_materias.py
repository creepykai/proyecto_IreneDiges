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

        try:
            materia: Materia = Materia(id_materia,materia_nombre, departamento)
        except ValueError as error:
            print("Error al crear la materia", error)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        insertar = (
                "INSERT INTO materias (id, materia, departamento) "
                "VALUES ('" + materia.id + "', '" + materia.materia + "', '" + materia.departamento + "')")

        try:
            conexion_bd.ejecutar_consulta(insertar)
            print("Materia creada con exito")
        except:
            print("No se ha podido guardar la materia en la BDD")

        conexion_bd.cerrar()
        return materia

    def modificar_materia(self, materia: Materia) -> None:
        nuevo_nombre: str = ""
        nuevo_departamento: str = ""

        nombre_final: str = materia.materia
        departamento_final: str = materia.departamento

        nuevo_nombre = input(
            "Introduce el nuevo nombre de la materia / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_nombre != "":
            nombre_final = nuevo_nombre

        nuevo_departamento = input("Introduce el nuevo departamento / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_departamento != "":
            departamento_final = nuevo_departamento

        try:
            materia_temporal = Materia(materia.id, nombre_final, departamento_final)
        except ValueError as e:
            print("Error al modificar la materia:", e)
            return

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update_materia = ("UPDATE materias SET materia = '" + nombre_final + "', departamento = '" + departamento_final +
                "' WHERE id = " + str(materia.id))

        try:
            conexion_bd.ejecutar_consulta(update_materia)
            print("La materia se ha modificado correctamente.")
        except:
            print("Error al modificar la materia en la base de datos.")
        finally:
            conexion_bd.cerrar()