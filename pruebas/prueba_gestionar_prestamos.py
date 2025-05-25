import unittest
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from clases.prestamo import Prestamo
from controladores.gestionar_prestamos import GestionarPrestamo

class TestGestionarPrestamo(unittest.TestCase):
    def setUp(self):
        self.alumno = Alumno("12345678A", "Juan", "Pérez", "I", True)
        self.libro = Libro("9783161484100", "Física y Química", "Autor X", 5, "1", "1ESO")
        self.curso = Curso("1ESO", "ESO")

    def test_crear_prestamo_objeto(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        self.assertEqual(prestamo.alumno.nie, "12345678A")
        self.assertEqual(prestamo.libro.isbn, "9783161484100")
        self.assertEqual(prestamo.curso.curso, "1ESO")
        self.assertEqual(prestamo.estado, "P")

    def test_modificar_prestamo_datos(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        prestamo.modificar_datos(curso=Curso("2ESO", "ESO"), fecha_devolucion="2025-06-15", estado="D")
        self.assertEqual(prestamo.curso.curso, "2ESO")
        self.assertEqual(prestamo.fecha_devolucion, "2025-06-15")
        self.assertEqual(prestamo.estado, "D")

    def test_str_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "D", "2025-06-15")
        esperado = (
            "Alumno: Juan Pérez Libro: Física y Química Curso: 1ESO, Nivel: ESO "
            "Fecha entrega: 2025-06-01 Fecha devolución: 2025-06-15 Estado: Devuelto"
        )
        self.assertEqual(str(prestamo), esperado)

    def test_validar_datos_correctos(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        self.assertTrue(prestamo.validar_datos_prestamo())

    def test_validar_datos_incorrectos(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        with self.assertRaises(ValueError):
            prestamo.estado = "X"

if __name__ == "__main__":
    unittest.main()
