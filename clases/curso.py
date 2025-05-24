class Curso:
    def __init__(self, curso: str, nivel: str):
        self.curso = curso
        self.nivel = nivel

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "":
            raise ValueError("El campo 'curso' no puede estar vacío.")
        if not Curso.contiene_letras(valor):
            raise ValueError("El campo 'curso' debe contener al menos una letra.")
        self._curso = valor

    @property
    def nivel(self) -> str:
        return self._nivel

    @nivel.setter
    def nivel(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "":
            raise ValueError("El campo 'nivel' no puede estar vacío.")
        if not Curso.contiene_letras(valor):
            raise ValueError("El campo 'nivel' debe contener al menos una letra.")
        self._nivel = valor

    @staticmethod
    def contiene_letras(texto: str) -> bool:
        return any(c.isalpha() for c in texto)

    def __str__(self) -> str:
        return f"Curso: {self.curso}, Nivel: {self.nivel}"
