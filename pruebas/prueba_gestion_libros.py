import unittest
from clases.libro import Libro
from controladores.gestionar_libros import GestionarLibro

class TestLibro(unittest.TestCase):
    def test_crear_libro_valido(self):
        libro = Libro("9783161484100", "Física y Química 1º ESO", "Autor X", 10, "Editorial XYZ", "Física", "1ºESO")
        self.assertEqual(libro.isbn, "9783161484100")
        self.assertEqual(libro.titulo, "Física y Química 1º ESO")
        self.assertEqual(libro.autor, "Autor X")
        self.assertEqual(libro.editorial, "Editorial XYZ")
        self.assertEqual(libro.ejemplares, 10)
        self.assertEqual(libro.materia, "Física")
        self.assertEqual(libro.curso, "1ºESO")

    def test_crear_libro_ingles(self):
        libro = Libro("9783161484101", "Inglés 2º ESO", "Autor Y", 5, "Editorial ABC", "Inglés", "2ºESO")
        self.assertEqual(libro.isbn, "9783161484101")
        self.assertEqual(libro.titulo, "Inglés 2º ESO")
        self.assertEqual(libro.autor, "Autor Y")
        self.assertEqual(libro.editorial, "Editorial ABC")
        self.assertEqual(libro.ejemplares, 5)
        self.assertEqual(libro.materia, "Inglés")
        self.assertEqual(libro.curso, "2ºESO")

    def test_ejemplares_negativos(self):
        with self.assertRaises(ValueError):
            Libro("9783161484102", "Libro sin ejemplares", "Autor Z", -3, "Editorial Test", "Historia", "3ºESO")

    def test_modificar_datos(self):
        libro = Libro("9783161484103", "Matemáticas 1º ESO", "Autor M", 12, "Editorial DEF", "Matemáticas", "1ºESO")
        libro.modificar_datos("Matemáticas Avanzadas", "Autor M", 15, "Editorial DEF", "Matemáticas", "1ºESO")
        self.assertEqual(libro.titulo, "Matemáticas Avanzadas")
        self.assertEqual(libro.ejemplares, 15)

    def test_str(self):
        libro = Libro("9783161484104", "Ciencias Naturales", "Autor N", 8, "Editorial GHI", "Ciencias", "2ºESO")
        esperado = "ISBN: 9783161484104 Título: Ciencias Naturales Autor: Autor N Ejemplares: 8 Editorial: Editorial GHI Materia: Ciencias Curso: 2ºESO"
        self.assertEqual(str(libro), esperado)

    def test_set_isbn_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.isbn = "123"

    def test_set_titulo_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.titulo = ""

    def test_set_autor_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.autor = ""

    def test_set_editorial_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.editorial = ""

    def test_set_materia_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.materia = ""

    def test_set_curso_invalido(self):
        libro = Libro("9783161484100", "Título", "Autor", 1, "Editorial", "Materia", "Curso")
        with self.assertRaises(ValueError):
            libro.curso = ""

if __name__ == "__main__":
    unittest.main()
