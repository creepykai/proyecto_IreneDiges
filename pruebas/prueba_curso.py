import unittest
from clases.curso import Curso

class TestCurso(unittest.TestCase):
    def test_crear_curso_valido(self):
        curso = Curso("3ºESO", "ESO")
        self.assertEqual(curso.curso, "3ºESO")
        self.assertEqual(curso.nivel, "ESO")

    def test_crear_curso_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Curso("", "ESO")

    def test_crear_curso_nivel_vacio(self):
        with self.assertRaises(ValueError):
            Curso("3ºESO", "")

    def test_crear_curso_nombre_sin_letras(self):
        with self.assertRaises(ValueError):
            Curso("12345", "ESO")

    def test_crear_curso_nivel_sin_letras(self):
        with self.assertRaises(ValueError):
            Curso("3ºESO", "1234")

    def test_str(self):
        curso = Curso("3ºESO", "ESO")
        self.assertEqual(str(curso), "Curso: 3ºESO, Nivel: ESO")

    def test_set_curso_invalido(self):
        curso = Curso("1ºESO", "ESO")
        with self.assertRaises(ValueError):
            curso.curso = "12345"
        with self.assertRaises(ValueError):
            curso.nivel = "1234"

if __name__ == "__main__":
    unittest.main()
