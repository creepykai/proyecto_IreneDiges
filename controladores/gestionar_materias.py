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
        nombre_final: str = ""
        departamento_final: str = ""

        nuevo_nombre = input("Introduce el nuevo nombre de la materia / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_departamento = input("Introduce el nuevo departamento / Dejar vacío si no se quiere modificar: ").strip()

        nombre_final = materia.materia if nuevo_nombre == "" else nuevo_nombre
        departamento_final = materia.departamento if nuevo_departamento == "" else nuevo_departamento

        try:
            materia_temp = Materia(materia.id, nombre_final, departamento_final)
        except ValueError as error:
            print("Error al modificar la materia:", error)
            return

        materia.materia = materia_temp.materia
        materia.departamento = materia_temp.departamento

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update = (
                "UPDATE materias SET materia = '" + materia.materia +
                "', departamento = '" + materia.departamento +
                "' WHERE id = " + str(materia.id)
        )

        try:
            conexion_bd.ejecutar_consulta(update)
            print("La materia se ha modificado correctamente.")
        except:
            print("No se pudo modificar la materia en la base de datos.")

        conexion_bd.cerrar()