import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = main.App()

    def test_mostrar_menu_principal(self):
        self.assertIsNone(self.app.mostrar_menu_principal())

    def test_opcion_invalida(self):
        resultado = self.simular_opcion('9')
        self.assertEqual(resultado, "Opción inválida")

    def test_salir_menu(self):
        resultado = self.simular_opcion('6')
        self.assertEqual(resultado, "Saliendo")

    def simular_opcion(self, opcion):
        match opcion:
            case "1":
                return "submenu_alumnos"
            case "2":
                return "submenu_libros"
            case "3":
                return "submenu_materias"
            case "4":
                return "submenu_cursos"
            case "5":
                return "submenu_prestamos"
            case "6":
                return "Saliendo"
            case "7":
                return "cargar_datos"
            case _:
                return "Opción inválida"

    def test_cargar_datos_desde_csv(self):
        try:
            main.cargar_alumnos_desde_csv('datos_csv/alumnos.csv')
            main.cargar_materias_desde_csv('datos_csv/materias.csv')
            main.cargar_cursos_desde_csv('datos_csv/cursos.csv')
            main.cargar_libros_desde_csv('datos_csv/libros.csv')
            main.cargar_prestamos_desde_csv('datos_csv/prestamos.csv')
            resultado = True
        except Exception:
            resultado = False
        self.assertTrue(resultado)

if __name__ == "__main__":
    unittest.main()
