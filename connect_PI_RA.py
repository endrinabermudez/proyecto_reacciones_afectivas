import sqlite3

def connect_sqlite():
    conexion = sqlite3.connect("Proyecto_Integrador.db")
    return conexion
print("Conexión realizada correctamente")

def disconnect_sqlite(conexion):
    conexion.close()
    print("Desconectado correctamente")