import unittest
from clases.alumno import Alumno
from controladores.gestionar_alumnos import GestionarAlumnos

class TestGestionarAlumnos(unittest.TestCase):
    def setUp(self):
        self.gestor = GestionarAlumnos()

    def test_crear_alumno_valido(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        self.assertEqual(alumno.nie, "03556632D")
        self.assertEqual(alumno.nombre, "Manuel")
        self.assertEqual(alumno.apellidos, "García")
        self.assertEqual(alumno.tramo, "I")
        self.assertTrue(alumno.bilingue)

    def test_crear_alumno_nie_invalido(self):
        with self.assertRaises(ValueError):
            Alumno("123", "Manuel", "García", "I", True)

    def test_modificar_datos(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        alumno.modificar_datos("Juan", "Pérez", "II", False)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellidos, "Pérez")
        self.assertEqual(alumno.tramo, "II")
        self.assertFalse(alumno.bilingue)

    def test_str_alumno(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        esperado = "NIE: 03556632D Nombre: Manuel Apellidos: García Tramo: I Bilingüe: Sí"
        self.assertEqual(str(alumno), esperado)

    def test_set_nombre_invalido(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        with self.assertRaises(ValueError):
            alumno.nombre = "1234"

    def test_set_apellidos_invalido(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        with self.assertRaises(ValueError):
            alumno.apellidos = "1234"

    def test_set_tramo_invalido(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        with self.assertRaises(ValueError):
            alumno.tramo = "III"

    def test_set_bilingue_no_bool(self):
        alumno = Alumno("03556632D", "Manuel", "García", "I", True)
        with self.assertRaises(ValueError):
            alumno.bilingue = "sí"

    def test_nie_formato_invalido(self):
        with self.assertRaises(ValueError):
            Alumno("ABCDEFGH1", "Manuel", "García", "I", True)

    def test_nombre_con_espacios_y_acentos(self):
        alumno = Alumno("03556632D", "José Luis", "Pérez Gómez", "I", True)
        self.assertEqual(alumno.nombre, "José Luis")
        self.assertEqual(alumno.apellidos, "Pérez Gómez")


if __name__ == "__main__":
    unittest.main()
