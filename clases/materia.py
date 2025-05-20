class Materia:
    def __init__(self, materia: str, departamento: str):
        self.materia = materia
        self.departamento = departamento

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
            self.materia = self.materia  # Llama al setter para validar
            self.departamento = self.departamento
            return True
        except ValueError as error:
            print(f"Error {error}")
            return False

    def __str__(self) -> str:
        return f"Materia: {self.materia} Departamento: {self.departamento}"
