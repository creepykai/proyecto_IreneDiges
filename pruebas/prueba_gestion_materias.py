import unittest
from clases.materia import Materia
from controladores.gestionar_materias import GestionarMaterias

class TestGestionarMaterias(unittest.TestCase):
    def setUp(self):
        self.gestor = GestionarMaterias()

    def test_crear_materia_valida(self):
        materia = Materia(1, "Matemáticas", "Ciencias Exactas")
        self.assertEqual(materia.id, 1)
        self.assertEqual(materia.materia, "Matemáticas")
        self.assertEqual(materia.departamento, "Ciencias Exactas")

    def test_materia_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Materia(2, "", "Ciencias Exactas")

    def test_departamento_vacio(self):
        with self.assertRaises(ValueError):
            Materia(3, "Matemáticas", "")

    def test_modificar_materia(self):
        materia = Materia(4, "Inglés", "Idiomas")
        materia.materia = "Francés"
        materia.departamento = "Idiomas Extranjeros"
        self.assertEqual(materia.materia, "Francés")
        self.assertEqual(materia.departamento, "Idiomas Extranjeros")

    def test_str_materia(self):
        materia = Materia(5, "Física", "Ciencias Naturales")
        esperado = "Materia: Física Departamento: Ciencias Naturales"
        self.assertEqual(str(materia), esperado)

if __name__ == "__main__":
    unittest.main()
