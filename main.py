from controladores.gestionar_alumnos import crear_alumno, modificar_alumno
from controladores.gestionar_libros import crear_libro, modificar_libro
from controladores.gestionar_cursos import crear_curso, modificar_curso
from controladores.gestionar_materias import crear_materia, modificar_materia
from controladores.gestionar_prestamos import crear_prestamo, modificar_prestamo

class App:
    def mostrar_menu(self):
        print("MENÚ PRINCIPAL")
        print("1. Crear alumno")
        print("2. Modificar alumno")
        print("3. Crear libro")
        print("4. Modificar libro")
        print("5. Crear curso")
        print("6. Modificar curso")
        print("7. Crear materia")
        print("8. Modificar materia")
        print("9. Crear préstamo")
        print("10. Modificar préstamo")
        print("0. Salir")

    def obtener_indice(self, lista, mensaje):
        try:
            seleccion = int(input(mensaje)) - 1
            if 0 <= seleccion < len(lista):
                return seleccion
            else:
                print("Número fuera de rango.")
        except:
            print("Entrada no válida. Debes introducir un número")
        return None

    def main(self):
        alumnos = []
        libros = []
        cursos = []
        materias = []
        prestamos = []

        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opcion: ").strip()

            match opcion:
                case "1":
                    alumno = crear_alumno()
                    if alumno is not None:
                        alumnos.append(alumno)

                case "2":
                    if not alumnos:
                        print("No hay alumnos registrados.")
                    else:
                        for i, alumno in enumerate(alumnos):
                            print(f"{i + 1}. {alumno}")
                        seleccion = self.obtener_indice(alumnos, "Escribe el número de alumno que quieres modificar: ")
                        if seleccion is not None:
                            modificar_alumno(alumnos[seleccion])

                case "3":
                    libro = crear_libro()
                    if libro is not None:
                        libros.append(libro)

                case "4":
                    if not libros:
                        print("No hay libros registrados.")
                    else:
                        for indice, libro in enumerate(libros):
                            print(f"{indice + 1}. {libro}")
                        seleccion = self.obtener_indice(libros, "Selecciona el número de libro que quieres modificar: ")
                        if seleccion is not None:
                            modificar_libro(libros[seleccion])

                case "5":
                    curso = crear_curso()
                    if curso is not None:
                        cursos.append(curso)

                case "6":
                    if not cursos:
                        print("No hay cursos registrados.")
                    else:
                        for indice, curso in enumerate(cursos):
                            print(f"{indice + 1}. {curso}")
                        seleccion = self.obtener_indice(cursos, "Selecciona el número de curso que quieres modificar: ")
                        if seleccion is not None:
                            modificar_curso(cursos[seleccion])

                case "7":
                    materia = crear_materia()
                    if materia is not None:
                        materias.append(materia)

                case "8":
                    if not materias:
                        print("No hay materias registrados.")
                    else:
                        for indice, materia in enumerate(materias):
                            print(f"{indice + 1}. {materia}")
                        seleccion = self.obtener_indice(materias, "Selecciona el número de materia que quieres modificar: ")
                        if seleccion is not None:
                            modificar_materia(materias[seleccion])

                case "9":
                    if not alumnos or not libros or not cursos:
                        print("Faltan datos necesarios (alumnos, libros o cursos).")
                    else:
                        for i, alumno in enumerate(alumnos):
                            print(f"{i + 1}. {alumno}")
                        alumno_indice = self.obtener_indice(alumnos, "Selecciona el número de alumno: ")
                        if alumno_indice is None:
                            continue

                        for i, libro in enumerate(libros):
                            print(f"{i + 1}. {libro}")
                        libro_indice = self.obtener_indice(libros, "Selecciona el número de libro: ")
                        if libro_indice is None:
                            continue

                        for i, curso in enumerate(cursos):
                            print(f"{i + 1}. {curso}")
                        curso_indice = self.obtener_indice(cursos, "Selecciona el número de curso: ")
                        if curso_indice is None:
                            continue

                        prestamo = crear_prestamo()
                        if prestamo is not None:
                            prestamos.append(prestamo)

                case "10":
                    if not prestamos:
                        print("No hay prestamos registrados.")
                    else:
                        for indice, prestamo in enumerate(prestamos):
                            print(f"{indice + 1}. {prestamo}")
                        seleccion = self.obtener_indice(prestamos, "Selecciona el número de préstamos que quieres modificar:")
                        if seleccion is not None:
                            modificar_prestamo(prestamos[seleccion])

                case "0":
                    break

                case _:
                    print("Opcion invalida")


if __name__ == "__main__":
    app = App()
    app.main()






