from conexion_bd import ConexionBD

bd = ConexionBD()
bd.conectar_base_de_datos()

consulta = "SELECT * FROM alumnos"
resultados = bd.obtener_datos(consulta)

for fila in resultados:
    print(fila)

bd.cerrar()
