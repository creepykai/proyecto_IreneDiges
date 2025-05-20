class Alumno:
    def __init__(self, nie : str, nombre : str, apellidos : str, tramo : str, bilingue : bool):
        self._nie = nie
        self._nombre = nombre
        self._apellidos = apellidos
        self._tramo = tramo
        self._bilingue = bilingue

    @property
    def nie(self) -> str:
        return self._nie

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor : str):
        if valor.strip() == "" or Alumno.contiene_numeros(valor.replace(" ", "")):
            raise ValueError("El nombre no puede estar vacío ni contener números")
        self._nombre = valor

    @property
    def apellidos(self) -> str:
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor : str) -> None:
        if valor.strip() == "":
            raise ValueError("Los apellidos no pueden estar vacios.")
        self._apellidos = valor

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

    def modificar_datos(self, nombre = None, apellidos = None, tramo = None, bilingue = None) -> None:
        if nombre is not None:
            self.nombre = nombre
        if apellidos is not None:
            self.apellidos = apellidos
        if tramo is not None:
            self.tramo = tramo
        if bilingue is not None:
            self.bilingue = bilingue

    def validar_nie(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if len(self.nie) != 9:
            mensaje_error = "El NIE debe tener 8 dígitos y una letra."
            es_valido = False
        else:
            solo_numeros: bool = True
            letra_final: str = ""
            i: int = 0

            while i < 8 and solo_numeros:
                if self.nie[i] not in "0123456789":
                    solo_numeros = False
                i += 1

            letra_final = self.nie[8]

            if not solo_numeros or Alumno.contiene_numeros(letra_final):
                mensaje_error = "El NIE debe tener 8 números seguidos de una letra."
                es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_nombre(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        nombre_sin_espacios: str = ""

        nombre_sin_espacios = self.nombre.replace(" ", "")

        if self.nombre.strip() == "":
            mensaje_error = "El nombre no puede estar vacío."
            es_valido = False
        elif Alumno.contiene_numeros(nombre_sin_espacios):
            mensaje_error = "El nombre no puede contener números."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_apellidos(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        apellidos_sin_espacios: str = ""

        apellidos_sin_espacios = self.apellidos.replace(" ", "")

        if self.apellidos.strip() == "":
            mensaje_error = "Los apellidos no pueden estar vacíos."
            es_valido = False
        elif Alumno.contiene_numeros(apellidos_sin_espacios):
            mensaje_error = "Los apellidos no pueden contener números."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_tramo(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        tramo_mayus: str = ""

        tramo_mayus = self.tramo.strip().upper()

        if tramo_mayus == "":
            mensaje_error = "El tramo no puede estar vacío."
            es_valido = False
        elif tramo_mayus not in ["0", "I", "II"]:
            mensaje_error = "El tramo debe ser 0, I o II."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_bilingue(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if type(self.bilingue) is not bool:
            mensaje_error = "El campo bilingüe debe ser Verdadero o Falso (bool)."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validacion_datos_alumno(self) -> bool:
        es_valido: bool = True

        if not self.validar_nie():
            es_valido = False
        if not self.validar_nombre():
            es_valido = False
        if not self.validar_apellidos():
            es_valido = False
        if not self.validar_tramo():
            es_valido = False
        if not self.validar_bilingue():
            es_valido = False

        return es_valido


    def __str__(self):
        bilingue_str = ""

        bilingue_str = "Sí" if self.bilingue else "No"

        return f"NIE: {self.nie} Nombre: {self.nombre} Apellidos: {self.apellidos} Tramo: {self.tramo} Bilingue: {bilingue_str}"

