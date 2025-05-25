import unittest
from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso
from clases.prestamo import Prestamo

class TestPrestamo(unittest.TestCase):
    def setUp(self):
        self.alumno = Alumno("12345678A", "Juan", "Pérez", "I", True)
        self.libro = Libro("9783161484100", "Física y Química", "Autor X", 5, "1", "1ESO")
        self.curso = Curso("1ESO", "ESO")

    def test_crear_prestamo_valido(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        self.assertEqual(prestamo.alumno.nie, "12345678A")
        self.assertEqual(prestamo.libro.titulo, "Física y Química")
        self.assertEqual(prestamo.curso.curso, "1ESO")
        self.assertEqual(prestamo.estado, "P")

    def test_modificar_prestamo_completo(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        prestamo.modificar_datos(curso=Curso("2ESO", "ESO"), fecha_devolucion="2025-06-15", estado="D")
        self.assertEqual(prestamo.curso.curso, "2ESO")
        self.assertEqual(prestamo.fecha_devolucion, "2025-06-15")
        self.assertEqual(prestamo.estado, "D")

    def test_modificar_prestamo_parcial(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        prestamo.modificar_datos(estado="D")
        self.assertEqual(prestamo.estado, "D")
        self.assertEqual(prestamo.fecha_devolucion, "")

    def test_fecha_devolucion_none(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", None)
        self.assertIsNone(prestamo.fecha_devolucion)

    def test_str_representacion(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "D", "2025-06-15")
        esperado = (
            "Alumno: Juan Pérez Libro: Física y Química Curso: 1ESO, Nivel: ESO "
            "Fecha entrega: 2025-06-01 Fecha devolución: 2025-06-15 Estado: Devuelto"
        )
        self.assertEqual(str(prestamo), esperado)

    def test_validar_fecha_correcta(self):
        self.assertTrue(Prestamo.validar_fecha("2025-06-01", "fecha de prueba"))

    def test_validar_fecha_incorrecta(self):
        self.assertFalse(Prestamo.validar_fecha("01-06-2025", "fecha de prueba"))

    def test_validar_datos_prestamo_correcto(self):
        prestamo = Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "")
        self.assertTrue(prestamo.validar_datos_prestamo())

    def test_validar_datos_prestamo_incorrecto_fecha(self):
        # Aquí verificamos que lanzar el constructor con fecha mal formada levanta error
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "P", "fecha_mal")

    def test_estado_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            Prestamo(self.alumno, self.libro, self.curso, "2025-06-01", "X", "")

if __name__ == "__main__":
    unittest.main()
