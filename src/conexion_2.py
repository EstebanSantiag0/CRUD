import psycopg2
from psycopg2 import Error

DB_CONFIG = {
    "dbname": "sistema_escolar",
    "user":   "admin",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

def obtener_conexion():
    try:
        conexion = psycopg2.connect( **DB_CONFIG )
        return conexion
    except Error as e:
        print("No se conectó a la base de datos")
        return None

def ejecutar_sql(sql, params=None, es_select=False):
    conexion = obtener_conexion()
    if conexion == None:
        return None
    try:
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sql, params)
                if es_select:
                    return cursor.fetchall()
                return True
    except Error as e:
        print(f'no se ejecutó el comando {sql} --> {e}')
        return None
    finally:
        conexion.close()


def create(tabla, datos: dict):
    columnas = ", ".join(datos.keys())
    marcadores = ", ".join(["%s"] * len(datos))
    valores = tuple(datos.values())
    sql = f"INSERT INTO {tabla} ({columnas}) VALUES ({marcadores});"
    return ejecutar_sql(sql, params=valores)

def read(tabla, argumentos="*", adition=""):
    consulta = f"SELECT {argumentos} FROM {tabla} {adition};"
    resultados = ejecutar_sql(consulta, es_select=True)
    if resultados:
        columnas = list(zip(*resultados))
        return columnas
    return None

def update(tabla, datos: dict, condicion: str, params_condicion: tuple = ()):
    asignaciones = ", ".join([f"{col} = %s" for col in datos.keys()])
    valores = tuple(datos.values()) + params_condicion
    sql = f"UPDATE {tabla} SET {asignaciones} WHERE {condicion};"
    return ejecutar_sql(sql, params=valores)

def delete(tabla, condicion: str, params_condicion: tuple = ()):
    sql = f"DELETE FROM {tabla} WHERE {condicion};"
    return ejecutar_sql(sql, params=params_condicion)

if __name__ == "__main__":
    print(read("carrera", "carrera.nombre, count(*)", "join estudiante on estudiante.id_carrera = carrera.id group by carrera.nombre")[0])
    print(read("carrera", "carrera.nombre, count(*)", "join estudiante on estudiante.id_carrera = carrera.id group by carrera.nombre")[1])