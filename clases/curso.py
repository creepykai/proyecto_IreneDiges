class Curso:
    def __init__(self, curso: str, nivel: str):
        self.curso = curso
        self.nivel = nivel

    def contiene_letras(self, texto: str) -> bool:
        contiene: bool = False
        caracter: int = 0

        while caracter < len(texto) and not contiene:
            if texto[caracter] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                contiene = True
            caracter += 1

        return contiene

    def validar_curso(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if self.curso.strip() == "":
            mensaje_error = "El campo 'curso' no puede estar vacío."
            es_valido = False
        elif not self.contiene_letras(self.curso.strip()):
            mensaje_error = "El campo 'curso' debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_nivel(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if self.nivel.strip() == "":
            mensaje_error = "El campo 'nivel' no puede estar vacío."
            es_valido = False
        elif not self.contiene_letras(self.nivel.strip()):
            mensaje_error = "El campo 'nivel' debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_datos_curso(self) -> bool:
        es_valido: bool = True

        if not self.validar_curso():
            es_valido = False
        if not self.validar_nivel():
            es_valido = False

        return es_valido

    def __str__(self) -> str:
        return f"Curso: {self.curso}, Nivel: {self.nivel}"
