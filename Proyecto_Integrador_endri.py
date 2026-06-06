import pandas as pd
import pymysql
import sqlite3
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import connect_PI_RA
import matplotlib.pyplot as plt



# Conexión a la base de datos SQLite
conn = connect_PI_RA.connect_sqlite()

# Carga las tablas en memoria

usuarios = pd.read_sql_query("SELECT * FROM usuarios", conn)
reacciones = pd.read_sql_query("SELECT * FROM reacciones_afectivas", conn)
registros = pd.read_sql_query("SELECT * FROM registros_afectivos", conn)

# Muestra todos las tres tablas de la BD

""" print("\n" + "=" * 70)
print("TABLA USUARIOS")
print("=" * 70)
print(usuarios)

print("\n" + "=" * 70)
print("TABLA REACCIONES AFECTIVAS")
print("=" * 70)
print(reacciones)

print("\n" + "=" * 70)
print("TABLA REGISTROS AFECTIVOS")
print("=" * 70)
print(registros) """


# Formatea la fecha
registros["fecha_hora"] = pd.to_datetime(registros["fecha_hora"])

# Renombrar columnas antes del merge
usuarios = usuarios.rename(columns={"nombre": "nombre_usuario"})
reacciones = reacciones.rename(columns={"nombre": "nombre_reaccion"})

# Join entre las tres tablas
df = pd.merge(registros, usuarios, left_on="id_usuario", right_on="id_usuario")
df = pd.merge(df, reacciones, left_on="id_reaccion", right_on="id_reaccion")
#print(df.columns)
print(df[["nombre_usuario", "fecha_hora", "nombre_reaccion"]])

#usuarios y reacciones por día
""" usuarios_por_dia = df.groupby(df["fecha_hora"].dt.date)["id_usuario"].nunique()
usuarios_por_dia.columns = ["usuarios", "reacciones"]

#Grafico
usuarios_por_dia.plot(kind="bar", x="fecha_hora", y="nombre", legend=False)
plt.xlabel("Fecha")
plt.ylabel("Usuarios")
plt.title("Usuarios por día")
plt.show()  """

#reacciones por usuario
reacciones_por_usuario = df.groupby("nombre_reaccion")["id_usuario"].count().reset_index()
#print(reacciones_por_usuario)
reacciones_por_usuario.columns = ["nombre_reaccion", "usuarios"]

reacciones_por_usuario.plot(kind="bar", x="nombre_reaccion", y="usuarios", legend=False)
plt.xlabel("Reacciones")
plt.ylabel("Usuarios")
plt.title("Reacciones por usuario")
plt.show()

connect_PI_RA.disconnect_sqlite(conn)