class Libro:
    def __init__(self, isbn : str, titulo : str, editorial : str, materia : str, curso : str):
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial
        self.materia = materia
        self.curso = curso

    def modificar_datos(self, titulo = None, editorial = None, materia = None, curso = None) -> None:
        if titulo is not None:
            self.titulo = titulo
        if editorial is not None:
            self.editorial = editorial
        if materia is not None:
            self.materia = materia
        if curso is not None:
            self.curso = curso

    def contiene_letras(self, texto: str) -> bool:
        contiene: bool = False
        i: int = 0

        while i < len(texto) and not contiene:
            if texto[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                contiene = True
            i += 1

        return contiene

    def validar_isbn(self) -> bool:
        es_valido : bool = True
        mensaje_error : str = ""

        if self.isbn.strip() == "":
            mensaje_error = "El ISBN no puede estar vacio"
            es_valido = False
        elif len(self.isbn) != 13:
            mensaje_error = "El ISBN debe tener 13 caracteres"
            es_valido = False
        else:
            solo_digitos: bool = True
            caracter : int = 0

            while caracter < len(self.isbn) and solo_digitos:
                if self.isbn[caracter] not in "0123456789":
                    solo_digitos = False
                caracter += 1
            if not solo_digitos:
                mensaje_error = "El ISBN no puede estar vacio"
                es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_titulo(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        titulo_sin_espacios: str = ""

        titulo_sin_espacios = self.titulo.replace(" ", "")

        if self.titulo.strip() == "":
            mensaje_error = "El título no puede estar vacío."
            es_valido = False
        elif not self.contiene_letras(titulo_sin_espacios):
            mensaje_error = "El título debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_editorial(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        editorial_sin_espacios: str = ""

        editorial_sin_espacios = self.editorial.replace(" ", "")

        if self.editorial.strip() == "":
            mensaje_error = "La editorial no puede estar vacía."
            es_valido = False
        elif not self.contiene_letras(editorial_sin_espacios):
            mensaje_error = "La editorial debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_materia(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""
        materia_sin_espacios: str = ""

        materia_sin_espacios = self.materia.replace(" ", "")

        if self.materia.strip() == "":
            mensaje_error = "La materia no puede estar vacía."
            es_valido = False
        elif not self.contiene_letras(materia_sin_espacios):
            mensaje_error = "La materia debe contener al menos una letra."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido


    def __str__(self):
        return f"ISBN: {self.isbn} Título: {self.titulo} Editorial: {self.editorial} Materia: {self.materia} Curso: {self.curso}"

