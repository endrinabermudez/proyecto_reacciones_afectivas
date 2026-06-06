import pandas as pd
from sqlalchemy import create_engine

try:

    # Conexión con servidor local a base de datos
    
    engine = create_engine("mysql+pymysql://root:@localhost/Proyecto_Integrador")

    print("Conexión establecida correctamente.")


    # Carga las tablas en memoria

    usuarios = pd.read_sql_query("SELECT * FROM usuarios", engine)
    reacciones = pd.read_sql_query("SELECT * FROM reacciones_afectivas", engine)
    registros = pd.read_sql_query("SELECT * FROM registros_afectivos", engine)

   
    # Muestra todos las tres tablas de la BD

    print("\n" + "=" * 70)
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
    print(registros)

 
    # Formatea la fecha
    registros["fecha_hora"] = pd.to_datetime(registros["fecha_hora"])

  
    # Join entre las tres tablas
  
    registros_completos = registros.merge(
        usuarios, on="id_usuario", how="inner"
    ).merge(reacciones, on="id_reaccion", how="inner")

   
except Exception as e:
    print(f"\nError inesperado: {e}")

finally:
    print("\nConexión cerrada exitosamente.")
