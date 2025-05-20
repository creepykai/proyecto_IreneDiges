class Materia:
    def __init__(self, materia: str, departamento: str):
        self.materia = materia
        self.departamento = departamento

    def validar_materia(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if self.materia.strip() == "":
            mensaje_error = "El nombre de la materia no puede estar vacío."
            es_valido = False
        elif not Materia.contiene_letras(self.materia.strip()):
            mensaje_error = "El nombre de la materia debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")
        return es_valido

    def validar_departamento(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if self.departamento.strip() == "":
            mensaje_error = "El departamento no puede estar vacío."
            es_valido = False
        elif not Materia.contiene_letras(self.departamento.strip()):
            mensaje_error = "El departamento debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")
        return es_valido

    def validar_datos_materia(self) -> bool:
        es_valido: bool = True

        if not self.validar_materia():
            es_valido = False
        if not self.validar_departamento():
            es_valido = False

        return es_valido

    @staticmethod
    def contiene_letras(texto: str) -> bool:
        contiene: bool = False
        caracter: int = 0

        while caracter < len(texto) and not contiene:
            if texto[caracter] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                contiene = True
            caracter += 1

        return contiene


    def __str__(self) -> str:
        return f"Materia: {self.materia} Departamento: {self.departamento}"
