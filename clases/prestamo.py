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

    @property
    def alumno(self) -> Alumno:
        return self._alumno

    @alumno.setter
    def alumno(self, valor: Alumno) -> None:
        if not isinstance(valor, Alumno):
            raise ValueError("Debe asignarse un objeto de tipo Alumno.")
        self._alumno = valor

    @property
    def libro(self) -> Libro:
        return self._libro

    @libro.setter
    def libro(self, valor: Libro) -> None:
        if not isinstance(valor, Libro):
            raise ValueError("Debe asignarse un objeto de tipo Libro.")
        self._libro = valor

    @property
    def curso(self) -> Curso:
        return self._curso

    @curso.setter
    def curso(self, valor: Curso) -> None:
        self._curso = valor
        if not isinstance(valor, Curso):
            raise ValueError("Debe asignarse un objeto de tipo Curso.")
        self._curso = valor

    @property
    def fecha_entrega(self) -> str:
        return self._fecha_entrega

    @fecha_entrega.setter
    def fecha_entrega(self, valor: str) -> None:
        if not Prestamo.validar_fecha(valor, "fecha de entrega"):
            raise ValueError("Fecha de entrega no válida.")
        self._fecha_entrega = valor

    @property
    def fecha_devolucion(self) -> str:
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, valor: str) -> None:
        if valor is None:
            self._fecha_devolucion = None
            return
        if valor.strip() != "" and not Prestamo.validar_fecha(valor, "fecha de devolución"):
            raise ValueError("La fecha de devolución no es válida.")
        self._fecha_devolucion = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str) -> None:
        if valor not in ["P", "D"]:
            raise ValueError("El estado debe ser 'P' (prestado) o 'D' (devuelto).")
        self._estado = valor

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

    def modificar_datos(self, curso=None, fecha_devolucion=None, estado=None) -> None:
        if curso is not None:
            self.curso = curso
        if fecha_devolucion is not None:
            self.fecha_devolucion = fecha_devolucion
        if estado is not None:
            self.estado = estado

    def validar_datos_prestamo(self) -> bool:
        try:
            self.estado = self.estado
            self.fecha_entrega = self.fecha_entrega
            if self.fecha_devolucion.strip() != "":
                self.fecha_devolucion = self.fecha_devolucion
            return True
        except ValueError as error:
            print(f"Error: {error}")
            return False

    def __str__(self) -> str:
        estado_legible = "Prestado" if self.estado == "P" else "Devuelto"
        return (f"Alumno: {self.alumno.nombre} {self.alumno.apellidos} "
                f"Libro: {self.libro.titulo} "
                f"Curso: {self.curso.curso}, Nivel: {self.curso.nivel} "
                f"Fecha entrega: {self.fecha_entrega} "
                f"Fecha devolución: {self.fecha_devolucion} "
                f"Estado: {estado_legible}")



