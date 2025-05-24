import unittest
from clases.materia import Materia

class TestMateria(unittest.TestCase):

    def test_crear_materia_valida(self):
        materia = Materia(1, "Historia", "Ciencias Sociales")
        self.assertEqual(materia.id, 1)
        self.assertEqual(materia.materia, "Historia")
        self.assertEqual(materia.departamento, "Ciencias Sociales")

    def test_nombre_materia_vacio(self):
        with self.assertRaises(ValueError):
            Materia(2, "", "Ciencias Sociales")

    def test_departamento_vacio(self):
        with self.assertRaises(ValueError):
            Materia(3, "Historia", "")

    def test_str(self):
        materia = Materia(4, "Inglés", "Idiomas")
        esperado = "Materia: Inglés Departamento: Idiomas"
        self.assertEqual(str(materia), esperado)

if __name__ == '__main__':
    unittest.main()
