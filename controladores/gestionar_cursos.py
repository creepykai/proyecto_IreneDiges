from clases.curso import Curso

class GestionarCurso:
    def crear_curso(self) -> Curso:
        curso: str = ""
        nivel:str = ""

        nivel = input("Introduce el nivel del curso (ESO, Bachillerato:").strip()
        curso = input("Introduce el número de curso:").strip()

        curso_objeto: Curso = Curso(curso, nivel)

        if curso_objeto.validar_datos_curso():
            print("El curso se ha creado correctamente.")
            return curso_objeto
        else:
            print("No se ha podido crear el curso. Revisa los datos introducidos.")
            return None

    def modificar_curso(self, curso_objeto: Curso) -> None:
        nuevo_curso: str = ""
        nuevo_nivel: str = ""
        curso_final: str = ""
        nivel_final: str = ""

        nuevo_nivel = input("Introduce el nuevo nivel educativo (ESO, Bachillerato) / Dejar vacío para no modificar:").strip()
        nuevo_curso = input("Introduce el número de curso / Dejar vacio para no modificar:").strip()

        curso_final = curso_objeto.curso if nuevo_curso == "" else nuevo_curso
        nivel_final = curso_objeto.nivel if nuevo_nivel == "" else nuevo_nivel

        curso_temporal: Curso = Curso(curso_final, nivel_final)

        if curso_temporal.validar_datos_curso():
            curso_objeto.curso = curso_final
            curso_objeto.nivel = nivel_final
            print("El curso se ha modificado correctamente.")
        else:
            print("No se ha podido modificar el curso.")

