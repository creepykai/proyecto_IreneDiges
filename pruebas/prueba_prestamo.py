import unittest
from clases.prestamo import Prestamo
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        self.alumno = Alumno("03226649W", "Irene", "Diges", "I", False)
        self.libro = Libro("9783161484100", "Física y Química", "Autor X", 5, "Editorial A", "Física", "1ºESO")
        self.curso = Curso("1ºESO", "ESO")

    def test_crear_prestamo_valido(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        self.assertIsInstance(prestamo, Prestamo)

    def test_crear_prestamo_estado_invalido(self):
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "X", None)

    def test_crear_prestamo_sin_fecha_devolucion(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        self.assertIsNone(prestamo.fecha_devolucion)

    def test_fecha_entrega_vacia(self):
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "", "P", None)

    def test_fecha_entrega_mal_formateada(self):
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "01-06-2024", "P", None)

    def test_fecha_devolucion_mal_formateada(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        with self.assertRaises(ValueError):
            prestamo.modificar_datos(self.curso, "15-06-2024", "D")

    def test_str_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        esperado = ("Alumno: Irene Diges "
                    "Libro: Física y Química "
                    "Curso: 1ºESO, Nivel: ESO "
                    "Fecha entrega: 2024-06-01 "
                    "Fecha devolución: None "
                    "Estado: Prestado")
        self.assertEqual(str(prestamo), esperado)

    def test_modificar_datos_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        nuevo_curso = Curso("2ºESO", "ESO")
        prestamo.modificar_datos(nuevo_curso, "2024-06-15", "D")
        self.assertEqual(prestamo.curso.curso, "2ºESO")
        self.assertEqual(prestamo.fecha_devolucion, "2024-06-15")
        self.assertEqual(prestamo.estado, "D")

    def test_modificar_estado_invalido(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        nuevo_curso = Curso("2ºESO", "ESO")
        with self.assertRaises(ValueError):
            prestamo.modificar_datos(nuevo_curso, "2024-06-15", "X")

if __name__ == "__main__":
    unittest.main()
