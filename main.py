from controladores.gestionar_alumnos import GestionarAlumnos
from controladores.gestionar_libros import GestionarLibro
from controladores.gestionar_cursos import GestionarCurso
from controladores.gestionar_materias import GestionarMaterias
from controladores.gestionar_prestamos import GestionarPrestamo
from datos_csv.cargar_datos import (
    cargar_alumnos_desde_csv,
    cargar_libros_desde_csv,
    cargar_cursos_desde_csv,
    cargar_materias_desde_csv,
    cargar_prestamos_desde_csv
)

class App:
    def mostrar_menu_principal(self):
        print("MENÚ PRINCIPAL")
        print("1. Gestionar alumnos")
        print("2. Gestionar libros")
        print("3. Gestionar materias")
        print("4. Gestionar cursos")
        print("5. Gestionar préstamos")
        print("6. Salir")
        print("7. Cargar datos desde CSV")

    def submenu_alumnos(self):
        gestor = GestionarAlumnos()
        while True:
            print("SUBMENÚ ALUMNOS")
            print("1. Crear alumno")
            print("2. Modificar alumno")
            print("3. Buscar por NIE")
            print("4. Buscar por nombre")
            print("5. Buscar por tramo")
            print("6. Listar todos")
            print("7. Salir")
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    gestor.crear_alumno()
                case "2":
                    nie = input("Escribe el NIE del alumno que deseas modificar: ").upper()
                    gestor.modificar_alumno(nie)
                case "3":
                    nie = input("NIE a buscar: ").upper()
                    gestor.buscar_alumno_por_nie(nie)
                case "4":
                    nombre = input("Nombre a buscar: ")
                    gestor.buscar_alumnos_por_nombre(nombre)
                case "5":
                    tramo = input("Tramo a buscar: ")
                    gestor.buscar_alumnos_por_tramo(tramo)
                case "6":
                    gestor.listar_todos()
                case "7":
                    break
                case _:
                    print("Opción inválida")

    def submenu_libros(self):
        gestor = GestionarLibro()
        while True:
            print("SUBMENÚ LIBROS")
            print("1. Crear libro")
            print("2. Modificar libro")
            print("3. Buscar por ISBN")
            print("4. Buscar por autor")
            print("5. Buscar por materia")
            print("6. Listar todos")
            print("7. Salir")
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    gestor.crear_libro()
                case "2":
                    isbn = input("ISBN a modificar: ")
                    gestor.modificar_libro(isbn)
                case "3":
                    isbn = input("ISBN a buscar: ")
                    gestor.buscar_libro_por_isbn(isbn)
                case "4":
                    autor = input("Autor a buscar: ")
                    gestor.buscar_libros_por_autor(autor)
                case "5":
                    materia = input("Materia a buscar: ")
                    gestor.buscar_libros_por_materia(materia)
                case "6":
                    gestor.listar_todos()
                case "7":
                    break
                case _:
                    print("Opción inválida")

    def submenu_materias(self):
        gestor = GestionarMaterias()
        while True:
            print("SUBMENÚ MATERIAS")
            print("1. Crear materia")
            print("2. Modificar materia")
            print("3. Buscar por ID")
            print("4. Buscar por departamento")
            print("5. Listar todas")
            print("6. Salir")
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    gestor.crear_materia()
                case "2":
                    nombre = input("Nombre a modificar: ")
                    gestor.modificar_materia(nombre)
                case "3":
                    id_materia = input("ID a buscar: ")
                    gestor.buscar_materia_por_id(id_materia)
                case "4":
                    departamento = input("Departamento a buscar: ")
                    gestor.buscar_materias_por_departamento(departamento)
                case "5":
                    gestor.listar_todos()
                case "6":
                    break
                case _:
                    print("Opción inválida")

    def submenu_cursos(self):
        gestor = GestionarCurso()
        while True:
            print("SUBMENÚ CURSOS")
            print("1. Crear curso")
            print("2. Modificar curso")
            print("3. Buscar por nombre")
            print("4. Buscar por nivel")
            print("5. Listar todos")
            print("6. Salir")
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    gestor.crear_curso()
                case "2":
                    nombre = input("Nombre a modificar: ")
                    gestor.modificar_curso(nombre)
                case "3":
                    nombre = input("Nombre del curso a buscar: ")
                    gestor.buscar_curso_por_nombre(nombre)
                case "4":
                    nivel = input("Nivel a buscar: ")
                    gestor.buscar_cursos_por_nivel(nivel)
                case "5":
                    gestor.listar_todos()
                case "6":
                    break
                case _:
                    print("Opción inválida")

    def submenu_prestamos(self):
        gestor = GestionarPrestamo()
        while True:
            print("SUBMENÚ PRÉSTAMOS")
            print("1. Crear préstamo")
            print("2. Modificar préstamo")
            print("3. Buscar por NIE + ISBN")
            print("4. Buscar por estado")
            print("5. Listar todos")
            print("6. Generar contrato de préstamo")
            print("7. Salir")
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    gestor.crear_prestamo()
                case "2":
                    nie = input("NIE a modificar: ")
                    isbn = input("ISBN a modificar: ")
                    gestor.modificar_prestamo(nie, isbn)
                case "3":
                    nie = input("NIE a buscar: ")
                    isbn = input("ISBN a buscar: ")
                    gestor.buscar_prestamo_por_nie_isbn(nie, isbn)
                case "4":
                    estado = input("Estado a buscar (P/D): ")
                    gestor.buscar_prestamos_por_estado(estado)
                case "5":
                    gestor.listar_todos()
                case "6":
                    nie = input("NIE del préstamo: ").strip()
                    isbn = input("ISBN del préstamo: ").strip()
                    gestor.generar_contrato_prestamo(nie, isbn)
                case "7":
                    break
                case _:
                    print("Opción inválida")

    def main(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Elige una opción: ").strip()
            match opcion:
                case "1":
                    self.submenu_alumnos()
                case "2":
                    self.submenu_libros()
                case "3":
                    self.submenu_materias()
                case "4":
                    self.submenu_cursos()
                case "5":
                    self.submenu_prestamos()
                case "6":
                    print("Saliendo")
                    break
                case "7":
                    alumnos = cargar_alumnos_desde_csv('datos_csv/alumnos.csv')
                    libros = cargar_libros_desde_csv('datos_csv/libros.csv')
                    cursos = cargar_cursos_desde_csv('datos_csv/cursos.csv')
                    materias = cargar_materias_desde_csv('datos_csv/materias.csv')
                    prestamos = cargar_prestamos_desde_csv('datos_csv/prestamos.csv', alumnos, libros, cursos)
                    print("Datos cargados correctamente desde los CSV.")

                case _:
                    print("Opción inválida")

if __name__ == "__main__":
    app = App()
    app.main()
