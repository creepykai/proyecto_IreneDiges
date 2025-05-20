from clases.alumno import Alumno
from clases.libro import Libro
from clases.curso import Curso

class Prestamo:
    def __init__(self, alumno: Alumno, libro: Libro, curso: Curso, fecha_entrega: str, estado: str, fecha_devolucion: str = ""):
        self.alumno = alumno
        self.libro = libro
        self.curso = curso
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def modificar_datos(self, curso = None, fecha_devolucion = None, estado = None) -> None:
        if curso is not None:
            self.curso = curso
        if fecha_devolucion is not None:
            self.fecha_devolucion = fecha_devolucion
        if estado is not None:
            self.estado = estado

    def validar_estado(self) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if self.estado not in ["P", "D"]:
            mensaje_error = "El estado debe ser 'P' (prestado) o 'D' (devuelto)."
            es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def validar_datos_prestamo(self) -> bool:
        es_valido: bool = True

        if not self.validar_estado():
            es_valido = False

        if not Prestamo.validar_fecha(self.fecha_entrega, "fecha de entrega"):
            es_valido = False

        if self.fecha_devolucion.strip() != "":
            if not Prestamo.validar_fecha(self.fecha_devolucion, "fecha de devolución"):
                es_valido = False

        return es_valido

    @staticmethod
    def validar_fecha(fecha: str, campo: str) -> bool:
        es_valido: bool = True
        mensaje_error: str = ""

        if len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
            mensaje_error = f"La {campo} debe tener el formato AAAA-MM-DD."
            es_valido = False
        else:
            partes = fecha.split("-")
            if len(partes) != 3 or not (partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
                mensaje_error = f"La {campo} contiene caracteres no válidos."
                es_valido = False

        if not es_valido:
            print(f"Error: {mensaje_error}")

        return es_valido

    def __str__(self) -> str:
        estado_str: str = "Prestado" if self.estado == "P" else "Devuelto"

        return f"Alumno: {self.alumno.nombre} {self.alumno.apellidos} Libro: {self.libro.titulo} Curso: {self.curso} Fecha entrega: {self.fecha_entrega} Fecha devolución: {self.fecha_devolucion} Estado: {estado_str}"





