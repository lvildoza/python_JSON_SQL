import pyodbc
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_connection():
    try:
        connection = pyodbc.connect(
            driver=os.getenv("DB_DRIVER"),
            server=os.getenv("DB_SERVER"),
            database=os.getenv("DB_DATABASE"),
            uid=os.getenv("DB_USERNAME"),
            pwd=os.getenv("DB_PASSWORD")
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
