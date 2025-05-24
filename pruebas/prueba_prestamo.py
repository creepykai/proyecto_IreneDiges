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

    def test_str_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        esperado = (f"Alumno: {self.alumno.nie}, Libro: {self.libro.isbn}, "
                    f"Curso: {self.curso.curso}, Fecha entrega: 2024-06-01, "
                    f"Estado: P, Fecha devolución: None")
        self.assertEqual(str(prestamo), esperado)

    def test_modificar_datos_prestamo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        nuevo_curso = Curso("2ºESO", "ESO")
        prestamo.modificar_datos(nuevo_curso, "2024-06-15", "D")
        self.assertEqual(prestamo.estado, "D")
        self.assertEqual(prestamo.fecha_devolucion, "2024-06-15")

    def test_modificar_estado_invalido(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2024-06-01", "P", None)
        nuevo_curso = Curso("2ºESO", "ESO")
        with self.assertRaises(ValueError):
            prestamo.modificar_datos(nuevo_curso, "2024-06-15", "X")

if __name__ == '__main__':
    unittest.main()
