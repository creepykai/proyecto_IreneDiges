import unittest
from clases.libro import Libro

class TestLibro(unittest.TestCase):
    def test_crear_libro_valido(self):
        libro = Libro("9783161484100", "Física y Química 1º ESO", "Autor X", 10, "1", "1ESO")
        self.assertEqual(libro.isbn, "9783161484100")
        self.assertEqual(libro.titulo, "Física y Química 1º ESO")
        self.assertEqual(libro.autor, "Autor X")
        self.assertEqual(libro.ejemplares, 10)
        self.assertEqual(libro.materia, "1")
        self.assertEqual(libro.curso, "1ESO")

    def test_isbn_invalido(self):
        with self.assertRaises(ValueError):
            Libro("123", "Título", "Autor", 1, "1", "1ESO")

    def test_titulo_vacio(self):
        with self.assertRaises(ValueError):
            Libro("9783161484100", "", "Autor", 1, "1", "1ESO")

    def test_autor_vacio(self):
        with self.assertRaises(ValueError):
            Libro("9783161484100", "Título", "", 1, "1", "1ESO")

    def test_ejemplares_negativos(self):
        with self.assertRaises(ValueError):
            Libro("9783161484100", "Título", "Autor", -5, "1", "1ESO")

    def test_materia_vacia(self):
        with self.assertRaises(ValueError):
            Libro("9783161484100", "Título", "Autor", 1, "", "1ESO")

    def test_curso_vacio(self):
        with self.assertRaises(ValueError):
            Libro("9783161484100", "Título", "Autor", 1, "1", "")

    def test_modificar_datos(self):
        libro = Libro("9783161484100", "Título Original", "Autor Original", 5, "1", "1ESO")
        libro.modificar_datos(titulo="Título Nuevo", autor="Autor Nuevo", ejemplares=10, materia="2", curso="2ESO")
        self.assertEqual(libro.titulo, "Título Nuevo")
        self.assertEqual(libro.autor, "Autor Nuevo")
        self.assertEqual(libro.ejemplares, 10)
        self.assertEqual(libro.materia, "2")
        self.assertEqual(libro.curso, "2ESO")

    def test_str(self):
        libro = Libro("9783161484104", "Ciencias Naturales", "Autor N", 8, "5", "2ESO")
        esperado = "ISBN: 9783161484104 Título: Ciencias Naturales Autor: Autor N Ejemplares: 8 Materia: 5 Curso: 2ESO"
        self.assertEqual(str(libro), esperado)

if __name__ == "__main__":
    unittest.main()
