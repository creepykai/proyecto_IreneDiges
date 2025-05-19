import mysql.connector

class ConexionBD:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def conectar_base_de_datos(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bancolibros'
        )
        self.cursor = self.conexion.cursor()

    def ejecutar_consulta(self, consulta, valores = None):
        self.cursor.execute(consulta, valores)
        self.conexion.commit()

    def obtener_datos(self, consulta, valores = None):
        self.cursor.execute(consulta, valores)
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()



