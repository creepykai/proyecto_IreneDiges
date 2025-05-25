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

    def buscar_alumno_por_nie(self, nie):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnos WHERE nie = '" + nie + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("NIE:", fila[0], "Nombre:", fila[1], "Apellidos:", fila[2], "Tramo:", fila[3], "Bilingüe:", fila[4])
        else:
            print("Alumno no encontrado")
        conexion_bd.cerrar()

    def buscar_alumnos_por_nombre(self, nombre):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnos WHERE nombre LIKE '%" + nombre + "%'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("NIE:", fila[0], "Nombre:", fila[1], "Apellidos:", fila[2], "Tramo:", fila[3], "Bilingüe:",
                      fila[4])
        else:
            print("No se encontraron alumnos")
        conexion_bd.cerrar()

    def buscar_alumnos_por_tramo(self, tramo):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnos WHERE tramo = '" + tramo + "'"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("NIE:", fila[0], "Nombre:", fila[1], "Apellidos:", fila[2], "Tramo:", fila[3], "Bilingüe:",
                      fila[4])
        else:
            print("No se encontraron alumnos")
        conexion_bd.cerrar()

    def listar_todos(self):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnos"
        resultados = conexion_bd.obtener_datos(consulta)
        if resultados:
            for fila in resultados:
                print("NIE:", fila[0], "Nombre:", fila[1], "Apellidos:", fila[2], "Tramo:", fila[3], "Bilingüe:",
                      fila[4])
        else:
            print("No hay alumnos registrados")
        conexion_bd.cerrar()

    def modificar_alumno(self, nie):
        conexion_bd = ConexionBD()
        conexion_bd.conectar_base_de_datos()
        consulta = "SELECT * FROM alumnos WHERE nie = '" + nie + "'"
        resultado = conexion_bd.obtener_datos(consulta)
        if resultado:
            fila = resultado[0]
            print("NIE:", fila[0], "Nombre:", fila[1], "Apellidos:", fila[2], "Tramo:", fila[3], "Bilingüe:", fila[4])
            nombre_final = fila[1]
            apellidos_final = fila[2]
            tramo_final = fila[3]
            bilingue_final = bool(fila[4])

            nuevo_nombre = input("Nuevo nombre / Dejar vacío si no se modifica: ").strip()
            if nuevo_nombre != "":
                nombre_final = nuevo_nombre

            nuevo_apellido = input("Nuevo apellido / Dejar vacío si no se modifica: ").strip()
            if nuevo_apellido != "":
                apellidos_final = nuevo_apellido

            nuevo_tramo = input("Nuevo tramo (0, I, II) / Dejar vacío si no se modifica: ").strip().upper()
            if nuevo_tramo in ["0", "I", "II"]:
                tramo_final = nuevo_tramo

            nuevo_bilingue_str = input("¿Es bilingüe? (s/n) / Dejar vacío si no se modifica: ").strip().lower()
            if nuevo_bilingue_str in ["s", "n"]:
                bilingue_final = True if nuevo_bilingue_str == "s" else False

            bilingue_int = 1 if bilingue_final else 0

            consulta_update = "UPDATE alumnos SET nombre = '" + nombre_final + "', apellidos = '" + apellidos_final + "', tramo = '" + tramo_final + "', bilingue = " + str(
                bilingue_int) + " WHERE nie = '" + nie + "'"

            try:
                conexion_bd.ejecutar_consulta(consulta_update)
                print("El alumno se ha modificado correctamente.")
            except:
                print("Error al modificar el alumno en la base de datos.")
        else:
            print("Alumno no encontrado")
        conexion_bd.cerrar()
