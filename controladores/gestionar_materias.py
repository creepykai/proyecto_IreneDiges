from clases.materia import Materia

class GestionarMaterias:
    def crear_materia(self) -> Materia:
        materia: str = ""
        departamento: str = ""

        materia = input("Introduce el nombre de la materia: ").strip()
        departamento = input("Introduce el departamento al que pertenece: ").strip()

        materia_objeto: Materia = Materia(materia, departamento)

        if materia_objeto.validar_datos_materia():
            print("La materia se ha creado correctamente.")
            return materia_objeto
        else:
            print("No se ha podido crear la materia. Revisa los datos introducidos.")
            return None

    def modificar_materia(self, materia_objeto: Materia) -> None:
        nueva_materia: str = ""
        nuevo_departamento: str = ""
        materia_final: str = ""
        departamento_final: str = ""

        nueva_materia = input("Introduce el nuevo nombre de la materia / Dejar vacío si no se quiere modificar: ").strip()
        nuevo_departamento = input("Introduce el nuevo departamento / Dejar vacío si no se quiere modificar: ").strip()

        materia_final = materia_objeto.materia if nueva_materia == "" else nueva_materia
        departamento_final = materia_objeto.departamento if nuevo_departamento == "" else nuevo_departamento

        materia_temporal: Materia = Materia(materia_final, departamento_final)

        if materia_temporal.validar_datos_materia():
            materia_objeto.materia = materia_final
            materia_objeto.departamento = departamento_final
            print("La materia se ha modificado correctamente.")
        else:
            print("No se han guardado los cambios porque los datos no son válidos.")
