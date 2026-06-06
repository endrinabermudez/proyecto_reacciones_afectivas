import pandas as pd
import pymysql
import sqlite3
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import connect_PI_RA


# Conexión a la base de datos SQLite
conn = connect_PI_RA.connect_sqlite()
cursor = conn.cursor()

""" usuarios = [
(4, "Diana","Rose","dianar@yahoo.com","1970-11-12"),
(5, "Eduardo","García","eduardog@gmail.com","1985-03-20"),
(6, "Fernanda","López","fernandal@gmail.com","1990-07-15")     
]

cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?)", usuarios)

registros = [
(4, 4, 1, "2024-06-01 10:00:00"),
(5, 5, 2, "2024-06-01 11:00:00"),
(6, 6, 3, "2024-06-01 12:00:00")     
]
cursor.executemany("INSERT INTO registros_afectivos VALUES (?, ?, ?, ?)", registros)  """

cursor.execute("""
UPDATE registros_afectivos
SET id_reaccion = 1
WHERE id_registro = 6
""")

conn.commit()

connect_PI_RA.disconnect_sqlite(conn)