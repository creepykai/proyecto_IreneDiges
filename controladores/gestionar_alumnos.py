from clases.alumno import Alumno
from conexion_bd import ConexionBD

class GestionarAlumnos:
    def crear_alumno(self) -> Alumno:
        nie : str = ""
        nombre : str = ""
        apellido : str = ""
        tramo : str = ""
        bilingue_str : str = ""
        bilingue : bool = False

        nie : str = input("Ingrese el NIE del alumno (00000000X): ").strip().upper()
        nombre : str = input("Ingrese el nombre del alumno: ").strip()
        apellido : str = input("Ingrese el apellido del alumno: ").strip()
        tramo : str = input("Ingrese el tramo (0,I,II): ").strip().upper()

        bilingue_str= input("¿Es bilingüe? (s/n): ").strip().lower()

        if bilingue_str == "s":
            bilingue = True
        elif bilingue_str == "n":
            bilingue = False
        else:
            print("Entrada no válida para bilingüe. Se ha tomado como 'No bilingüe'")

        try:
            alumno: Alumno = Alumno(nie, nombre, apellido, tramo, bilingue)
        except ValueError as e:
            print("Error al crear el alumno:", e)
            return None

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        bilingue_int = 1 if alumno.bilingue else 0

        add_persona = ("INSERT INTO alumnos (nie, nombre, apellido, tramo, bilingue) "
                       "VALUES ('" + alumno.nie + "', '" + alumno.nombre + "', '" +
                       alumno.apellidos + "', '" + alumno.tramo + "', " + str(bilingue_int) + ")")

        print("Alumno añadido:", add_persona)

        try:
            conexion_bd.ejecutar_consulta(add_persona)
            print("El alumno se ha creado correctamente.")
        except:
            print("No se ha podido crear el alumno en la base de datos.")

        conexion_bd.cerrar()
        return alumno


    def modificar_alumno(self, alumno: Alumno) -> None:
        nuevo_nombre: str = ""
        nuevo_apellido: str = ""
        nuevo_tramo: str = ""
        nuevo_str_bilingue: str = ""
        bilingue_final: bool = alumno.bilingue
        bilingue_int: int = 0

        nuevo_nombre = input("Ingrese el nuevo nombre del alumno / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_apellido = input("Ingrese el nuevo apellido del alumno / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_tramo = input("Introduce el nuevo tramo: (0, I, II) / Dejar vacío si no se quiere modificar: ").strip().upper()
        nuevo_str_bilingue = input("¿Es bilingüe? (s/n) / Dejar vacío si no se quiere modificar: ").strip().lower()

        nombre_final = alumno.nombre if nuevo_nombre == "" else nuevo_nombre
        apellidos_final = alumno.apellidos if nuevo_apellido == "" else nuevo_apellido
        tramo_final = alumno.tramo if nuevo_tramo == "" else nuevo_tramo

        if nuevo_str_bilingue == "s":
            bilingue_final = True
        elif nuevo_str_bilingue == "n":
            bilingue_final = False

        alumno_temporal: Alumno = Alumno(alumno.nie, nombre_final, apellidos_final, tramo_final, bilingue_final)

        try:
            alumno_temporal: Alumno = Alumno(alumno.nie, nombre_final, apellidos_final, tramo_final, bilingue_final)
        except ValueError as e:
            print("Error al modificar el alumno:", e)
            return

        alumno.modificar_datos(nombre_final, apellidos_final, tramo_final, bilingue_final)

        bilingue_int = 1 if bilingue_final else 0

        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()

        mod_alumno = ( "UPDATE alumnos SET nombre = '" + nombre_final +
 "', apellido = '" + apellidos_final +
            "', tramo = '" + tramo_final +
            "', bilingue = " + str(bilingue_int) +
            " WHERE nie = '" + alumno.nie + "'")

        try:
            conexion_bd.ejecutar_consulta(mod_alumno)
            print("El alumno se ha modificado correctamente.")

        except:
            print("Error al modificar el alumno en la base de datos.")
        conexion_bd.cerrar()

