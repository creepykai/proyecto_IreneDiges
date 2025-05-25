import unittest
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from clases.prestamo import Prestamo
from controladores.gestionar_prestamos import GestionarPrestamo

class TestGestionarPrestamo(unittest.TestCase):
    def setUp(self):
        self.gestor = GestionarPrestamo()
        self.alumno = Alumno("03226649W", "Irene", "Diges", "I", False)
        self.libro = Libro("9783161484100", "Física y Química", "Autor X", 5, "Editorial A", "Física", "1ºESO")
        self.curso = Curso("1ºESO", "ESO")

    def test_crear_prestamo_valido(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", "")
        self.assertEqual(prestamo.alumno.nie, "03226649W")
        self.assertEqual(prestamo.libro.isbn, "9783161484100")
        self.assertEqual(prestamo.curso.curso, "1ºESO")
        self.assertEqual(prestamo.estado, "P")

    def test_estado_invalido(self):
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "X", "")

    def test_modificar_datos_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", "")
        nuevo_curso = Curso("2ºESO", "ESO")
        prestamo.modificar_datos(nuevo_curso, "2024-06-15", "D")
        self.assertEqual(prestamo.curso.curso, "2ºESO")
        self.assertEqual(prestamo.fecha_devolucion, "2024-06-15")
        self.assertEqual(prestamo.estado, "D")

    def test_str_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", "")
        resultado = str(prestamo)
        self.assertIn("Irene", resultado)
        self.assertIn("Física y Química", resultado)
        self.assertIn("1ºESO", resultado)

if __name__ == "__main__":
    unittest.main()
