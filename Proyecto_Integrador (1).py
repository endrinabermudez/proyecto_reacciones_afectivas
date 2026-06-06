import sqlite3

try:
    # Conexión a la base de datos
    conexion = sqlite3.connect("Proyecto_Integrador.db")
    cursor = conexion.cursor()

    print("Conexión establecida.")


    conexion.commit()

    # Mostrar usuarios
    print("\n=== USUARIOS ===")
    cursor.execute("SELECT * FROM usuarios")
    for fila in cursor.fetchall():
        print(fila)

    # Mostrar reacciones
    print("\n=== REACCIONES AFECTIVAS ===")
    cursor.execute("SELECT * FROM reacciones_afectivas")
    for fila in cursor.fetchall():
        print(fila)

    # Mostrar registros con JOIN
    print("\n=== REGISTROS AFECTIVOS ===")
    cursor.execute("""
    SELECT
        ra.id_registro,
        ra.fecha_hora,
        u.nombre || ' ' || u.apellido AS usuario,
        re.nombre AS reaccion,
        re.valencia,
        re.activacion
    FROM registros_afectivos ra
    JOIN usuarios u
        ON ra.id_usuario = u.id_usuario
    JOIN reacciones_afectivas re
        ON ra.id_reaccion = re.id_reaccion
    """)

    for fila in cursor.fetchall():
        print(fila)

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    if 'conexion' in locals():
        conexion.close()
        print("\nConexión cerrada.")
