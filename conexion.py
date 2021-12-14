import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def iniciarConexion(self):
        conexion = sqlite3.connect('sistema.s3db')
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion

    def leerContactos(self):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "SELECT * FROM contactos"
        cursor.execute(sentenciaSQL)
        return cursor.fetchall()

    def crearContactos(self, datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "INSERT INTO contactos(nombre,gmail) VALUES(?,?)"
        cursor.execute(sentenciaSQL, datosContacto)
        conexion.commit()
        conexion.close()

    def borrarContactos(self, idContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "DELETE FROM contactos WHERE id =(?)"
        cursor.execute(sentenciaSQL, [idContacto])
        conexion.commit()
        conexion.close()

    def modificarContactos(self, datosContacto):
        conexion = self.iniciarConexion()
        cursor = conexion.cursor()
        sentenciaSQL = "UPDATE contactos SET nombre=?, gmail=? WHERE id=?"
        cursor.execute(sentenciaSQL, datosContacto)
        conexion.commit()
        conexion.close()
