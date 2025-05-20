class Alumno:
    def __init__(self, nie: str, nombre: str, apellidos: str, tramo: str, bilingue: bool):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    @property
    def nie(self) -> str:
        return self._nie

    @nie.setter
    def nie(self, valor: str) -> None:
        valor = valor.strip().upper()
        if len(valor) != 9:
            raise ValueError("El NIE debe tener 9 caracteres (8 números y 1 letra).")

        numeros = valor[:8]
        letra = valor[8]

        if not numeros.isdigit():
            raise ValueError("Los primeros 8 caracteres del NIE deben ser números.")
        if not letra.isalpha():
            raise ValueError("El último carácter del NIE debe ser una letra.")

        self._nie = valor

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "":
            raise ValueError("El nombre no puede estar vacío.")
        if not valor.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras.")
        self._nombre = valor

    @property
    def apellidos(self) -> str:
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor: str) -> None:
        valor = valor.strip()
        if valor == "":
            raise ValueError("Los apellidos no pueden estar vacíos.")
        if not valor.replace(" ", "").isalpha():
            raise ValueError("Los apellidos solo pueden contener letras.")
        self._apellidos = valor

    @property
    def tramo(self) -> str:
        return self._tramo

    @tramo.setter
    def tramo(self, valor: str) -> None:
        valor = valor.strip().upper()
        if valor not in ["0", "I", "II"]:
            raise ValueError("El tramo debe ser 0, I o II.")
        self._tramo = valor

    @property
    def bilingue(self) -> bool:
        return self._bilingue

    @bilingue.setter
    def bilingue(self, valor: bool) -> None:
        if type(valor) is not bool:
            raise ValueError("El campo bilingüe debe ser Verdadero o Falso (bool).")
        self._bilingue = valor

    def modificar_datos(self, nombre=None, apellidos=None, tramo=None, bilingue=None) -> None:
        if nombre is not None:
            self.nombre = nombre
        if apellidos is not None:
            self.apellidos = apellidos
        if tramo is not None:
            self.tramo = tramo
        if bilingue is not None:
            self.bilingue = bilingue

    def __str__(self):
        bilingue_str = "Sí" if self.bilingue else "No"
        return f"NIE: {self.nie} Nombre: {self.nombre} Apellidos: {self.apellidos} Tramo: {self.tramo} Bilingüe: {bilingue_str}"
