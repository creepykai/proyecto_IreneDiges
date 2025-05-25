import unittest
from clases.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno_valido(self):
        alumno = Alumno("03556632D", "Manuel", "Sánchez", "I", False)
        self.assertEqual(alumno.nie, "03556632D")
        self.assertEqual(alumno.nombre, "Manuel")
        self.assertEqual(alumno.apellidos, "Sánchez")
        self.assertEqual(alumno.tramo, "I")
        self.assertFalse(alumno.bilingue)

    def test_crear_alumno_nie_invalido(self):
        with self.assertRaises(ValueError):
            Alumno("123", "Manuel", "Sánchez", "I", False)

    def test_crear_alumno_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Alumno("03556632D", "", "Sánchez", "I", False)

    def test_crear_alumno_apellido_vacio(self):
        with self.assertRaises(ValueError):
            Alumno("03556632D", "Manuel", "", "I", False)

    def test_crear_alumno_tramo_invalido(self):
        with self.assertRaises(ValueError):
            Alumno("03556632D", "Manuel", "Sánchez", "III", False)

    def test_modificar_datos(self):
        alumno = Alumno("03556632D", "Manuel", "Sánchez", "I", False)
        alumno.modificar_datos("Pedro", "García", "II", True)
        self.assertEqual(alumno.nombre, "Pedro")
        self.assertEqual(alumno.apellidos, "García")
        self.assertEqual(alumno.tramo, "II")
        self.assertTrue(alumno.bilingue)

    def test_str(self):
        alumno = Alumno("03556632D", "Manuel", "Sánchez", "I", False)
        self.assertIn("Manuel", str(alumno))
        self.assertIn("Sánchez", str(alumno))
        self.assertIn("I", str(alumno))

if __name__ == "__main__":
    unittest.main()
