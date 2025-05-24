from controladores.gestionar_alumnos import GestionarAlumnos
from controladores.gestionar_libros import  GestionarLibro
from controladores.gestionar_cursos import GestionarCurso
from controladores.gestionar_materias import GestionMaterias
from controladores.gestionar_prestamos import GestionarPrestamo

class App:
    def mostrar_menu_principal(self):
        print("MENÚ PRINCIPAL")
        print("1. Gestionar alumnos")
        print("2. Gestionar libros")
        print("3. Gestionar materias")
        print("4. Gestionar cursos")
        print("5. Gestionar prestamos")
        print("6. Salir")

    def submenu_alumnos(self):
        while True:
            print("Selecciona la acción que deseas: ")
            print("1. Crear alumno")
            print("2. Modificar alumno")
            print("3. Salir")

            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case "1":
                    crear_alumno()
                case "2":
                    nie = input("Introduce el numero de identificación escolar del alumno que quieres modificar: ")
                    modificar_alumno(nie)
                case "3":
                    break
                case _:
                    print("Opcion invalida")


    def submenu_libros(self):
        while True:
            print("Selecciona la accion que deseas:")
            print("1. Crear libro")
            print("2. Modificar libro")
            print("3. Salir")

            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case "1":
                    crear_libro()
                case "2":
                    isbn = input("Introduce el ISBN del libro que quieres modificar: ")
                    modificar_libro(isbn)
                case "3":
                    break
                case _:
                    print("Opcion invalida")


    def submenu_materias(self):
        while True:
            print("Selecciona la accion que deseas:")
            print("1. Crear materia")
            print("2. Modificar materia")
            print("3. Salir")

            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case "1":
                    crear_materia()
                case "2":
                    nombre = input("Introduce el nombre de la materia que quieres modificar: ")
                    modificar_materia(nombre)
                case "3":
                    break
                case _:
                    print("Opcion invalida")


    def submenu_cursos(self):
        while True:
            print("Selecciona la accion que deseas:")
            print("1. Crear curso")
            print("2. Modificar curso")
            print("3. Salir")

            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case "1":
                    crear_curso()
                case "2":
                    nombre = input("Introduce el nombre del curso que quieres modificar: ")
                    modificar_curso(nombre)
                case "3":
                    break
                case _:
                    print("Opcion invalida")


    def submenu_prestamos(self):
        while True:
            print("Selecciona la accion que deseas:")
            print("1. Crear prestamo")
            print("2. Modificar prestamo")
            print("3. Salir")

            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case "1":
                    crear_prestamo()
                case "2":
                    nie = input("Introduce el NIE del alumno del préstamo que quieres modificar: ").strip()
                    isbn = input("Introduce el ISBN del libro del préstamo que quieres modificar: ").strip()
                    modificar_prestamo(nie, isbn)
                case "3":
                    break
                case _:
                    print("Opcion invalida")


    def main(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Elige una opcion: ").strip()

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
                case _:
                    print("Opcion invalida")


if __name__ == "__main__":
    app = App()
    app.main()






