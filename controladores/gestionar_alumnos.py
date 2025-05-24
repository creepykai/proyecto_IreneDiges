from clases.alumno import Alumno
from conexion_bd import ConexionBD

class GestionarAlumnos:
    def crear_alumno(self) -> Alumno:
        nie = ""
        nombre = ""
        apellido = ""
        tramo = ""
        bilingue_str = ""
        bilingue = False

        while True:
            nie = input("Ingrese el NIE del alumno (00000000X): ").strip().upper()
            if len(nie) == 9 and nie[:8].isdigit() and nie[8].isalpha():
                break
            print("El NIE debe tener 8 números y una letra al final.")

        while True:
            nombre = input("Ingrese el nombre del alumno: ").strip()
            if nombre != "" and any(c.isalpha() for c in nombre):
                break
            print("El nombre no puede estar vacío y debe tener letras.")

        while True:
            apellido = input("Ingrese el apellido del alumno: ").strip()
            if apellido != "" and any(c.isalpha() for c in apellido):
                break
            print("El apellido no puede estar vacío y debe tener letras.")

        while True:
            tramo = input("Ingrese el tramo (0, I, II): ").strip().upper()
            if tramo in ["0", "I", "II"]:
                break
            print("El tramo debe ser 0, I o II.")

        while True:
            bilingue_str = input("¿Es bilingüe? (s/n): ").strip().lower()
            if bilingue_str in ["s", "n"]:
                bilingue = True if bilingue_str == "s" else False
                break
            print("Por favor, ingrese 's' para sí o 'n' para no.")

        try:
            alumno = Alumno(nie, nombre, apellido, tramo, bilingue)
        except ValueError as e:
            print("Error al crear el alumno:", e)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        bilingue_int = 1 if alumno.bilingue else 0

        add_persona = (
            "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) "
            "VALUES ('" + alumno.nie + "', '" + alumno.nombre + "', '" +
            alumno.apellidos + "', '" + alumno.tramo + "', " + str(bilingue_int) + ")")

        try:
            conexion_bd.ejecutar_consulta(add_persona)
            print("El alumno se ha creado correctamente.")
        except ValueError as error:
            print("No se ha podido crear el alumno en la base de datos. Error:", error)
        finally:
            conexion_bd.cerrar()

        return alumno

    def modificar_alumno(self, alumno: Alumno) -> None:
        nuevo_nombre: str = ""
        nuevo_apellido: str = ""
        nuevo_tramo: str = ""
        nuevo_str_bilingue: str = ""
        nombre_final: str = alumno.nombre
        apellidos_final: str = alumno.apellidos
        tramo_final: str = alumno.tramo
        bilingue_final: bool = alumno.bilingue

        nuevo_nombre = input("Introduce el nuevo nombre / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_nombre != "":
            nombre_final = nuevo_nombre

        nuevo_apellido = input("Introduce el nuevo apellido / Dejar vacío si no se quiere modificar: ").strip()
        if nuevo_apellido != "":
            apellido_final = nuevo_apellido

        nuevo_tramo = input(
            "Introduce el nuevo tramo (0, I, II) / Dejar vacío si no se quiere modificar: ").strip().upper()
        if nuevo_tramo in ["0", "I", "II"]:
            tramo_final = nuevo_tramo

        nuevo_bilingue_str = input("¿Es bilingüe? (s/n) / Dejar vacío si no se quiere modificar: ").strip().lower()
        if nuevo_bilingue_str in ["s", "n"]:
            bilingue_final = True if nuevo_bilingue_str == "s" else False
            bilingue_int = 1 if bilingue_final else 0

        try:
            alumno_temp = Alumno(alumno.nie, nombre_final, apellido_final, tramo_final, bilingue_final)
        except ValueError as error:
            print("Error al modificar el alumno:", eror)
            return

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        update_alumno = ("UPDATE alumnos SET nombre = '" + nombre_final + "', apellidos = '" + apellido_final +
                "', tramo = '" + tramo_final + "', bilingue = " + str(bilingue_int) + " WHERE nie = '" + alumno.nie + "'")

        try:
            conexion_bd.ejecutar_consulta(update_alumno)
            print("El alumno se ha modificado correctamente.")
        except:
            print("Error al modificar el alumno en la base de datos.")
        finally:
            conexion_bd.cerrar()