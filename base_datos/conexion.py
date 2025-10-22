import sqlite3


class Conexion:

  def __init__(self, nombre_bd):
    self.conexion = sqlite3.connect(nombre_bd)
    self.cursor = self.conexion.cursor()

  def crear_tabla_usuario(self):
    self.cursor.execute(
        "CREATE TABLE IF NOT EXISTS usuario(dni INTEGER, usuario TEXT, contrasena TEXT)"
    )
    self.conexion.commit()

  def agregar_usuario(self, dni, usuario, contrasena):
    self.cursor.execute("INSERT INTO cliente VALUES(?,?,?)",
                        (dni, usuario, contrasena))
    self.conexion.commit()

  def editar_usuario(self, dni, usuario, contrasena):
    self.cursor.execute(
        "UPDATE cliente SET dni=?, usuario=?, contrasena=? WHERE dni=?",
        (dni, usuario, contrasena, dni))
    self.conexion.commit()

  def mostrar_clientes(self):
    self.cursor.execute("SELECT * FROM usuario")
    clientes = self.cursor.fetchall()
    return clientes

  def eliminar_cliente(self, dni):
    self.cursor.execute("DELETE FROM usuario WHERE dni=?", (dni, ))
    self.conexion.commit()
  
  def cerrar_conexion(self):
    self.cursor.close()
    self.conexion.close()

