class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, ejemplares: int, editorial: str, materia: str, curso: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.editorial = editorial
        self.materia = materia
        self.curso = curso

    @property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "":
            raise ValueError("El ISBN no puede estar vacío.")
        if len(valor) != 13 or not valor.isdigit():
            raise ValueError("El ISBN debe tener 13 dígitos numéricos.")
        self._isbn = valor

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not Libro.contiene_letras(valor):
            raise ValueError("El título no puede estar vacío y debe contener letras.")
        self._titulo = valor

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not Libro.contiene_letras(valor):
            raise ValueError("El autor no puede estar vacío y debe contener letras.")
        self._autor = valor
    @property
    def ejemplares(self) -> int:
        return self._ejemplares

    @ejemplares.setter
    def ejemplares(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Los ejemplares deben ser un número entero mayor que cero.")
        self._ejemplares = valor

    @property
    def editorial(self) -> str:
        return self._editorial

    @editorial.setter
    def editorial(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not Libro.contiene_letras(valor):
            raise ValueError("La editorial no puede estar vacía y debe contener letras.")
        self._editorial = valor

    @property
    def materia(self) -> str:
        return self._materia

    @materia.setter
    def materia(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not Libro.contiene_letras(valor):
            raise ValueError("La materia no puede estar vacía y debe contener letras.")
        self._materia = valor

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not Libro.contiene_letras(valor):
            raise ValueError("El curso no puede estar vacío y debe contener letras.")
        self._curso = valor

    @staticmethod
    def contiene_letras(texto: str) -> bool:
        return any(caracter.isalpha() for caracter in texto)

    def __str__(self):
        return f"ISBN: {self.isbn} Título: {self.titulo} Autor: {self.autor} Ejemplares: {self.ejemplares} Editorial: {self.editorial} Materia: {self.materia} Curso: {self.curso}"

