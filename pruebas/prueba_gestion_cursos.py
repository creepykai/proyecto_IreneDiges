import unittest
from clases.curso import Curso
from controladores.gestionar_cursos import GestionarCurso

class TestGestionarCurso(unittest.TestCase):
    def setUp(self):
        self.gestor = GestionarCurso()

    def test_crear_curso_valido(self):
        curso = Curso("1ºESO", "ESO")
        self.assertEqual(curso.curso, "1ºESO")
        self.assertEqual(curso.nivel, "ESO")

    def test_crear_curso_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Curso("", "ESO")

    def test_crear_curso_nivel_vacio(self):
        with self.assertRaises(ValueError):
            Curso("1ºESO", "")

    def test_modificar_curso(self):
        curso = Curso("1ºESO", "ESO")
        curso.curso = "2ºESO"
        curso.nivel = "ESO"
        self.assertEqual(curso.curso, "2ºESO")
        self.assertEqual(curso.nivel, "ESO")

    def test_str_curso(self):
        curso = Curso("1ºESO", "ESO")
        esperado = "Curso: 1ºESO, Nivel: ESO"
        self.assertEqual(str(curso), esperado)

if __name__ == "__main__":
    unittest.main()
