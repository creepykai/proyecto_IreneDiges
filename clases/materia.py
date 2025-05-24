class Materia:
    def __init__(self,id : int, materia: str, departamento: str):
        self.id = id
        self.materia = materia
        self.departamento = departamento

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El id debe ser un número entero positivo.")
        self._id = valor

    @property
    def materia(self) -> str:
        return self._materia

    @materia.setter
    def materia(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not any(c.isalpha() for c in valor):
            raise ValueError("El nombre de la materia no puede estar vacío y debe contener al menos una letra.")
        self._materia = valor

    @property
    def departamento(self) -> str:
        return self._departamento

    @departamento.setter
    def departamento(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "" or not any(c.isalpha() for c in valor):
            raise ValueError("El departamento no puede estar vacío y debe contener al menos una letra.")
        self._departamento = valor

    def validar_datos_materia(self) -> bool:
        try:
            self.id = int(self.id)
            self.materia = self.materia
            self.departamento = self.departamento
            return True
        except ValueError as error:
            print(f"Error {error}")
            return False

    def __str__(self) -> str:
        return f"Materia: {self.materia} Departamento: {self.departamento}"
