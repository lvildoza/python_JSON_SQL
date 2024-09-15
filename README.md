# Proyecto: Conexión a Base de Datos SQL con Python

## Descripción

Este proyecto proporciona un ejemplo básico de cómo conectar una aplicación Python a una base de datos SQL utilizando la biblioteca `pyodbc`. El código muestra cómo ejecutar una consulta simple y recuperar resultados de la base de datos.

## Estructura de Archivos

- `main.py`: Archivo principal que establece la conexión a la base de datos y ejecuta una consulta.
- `database.py`: Módulo que contiene la lógica para obtener la conexión de la base de datos.
- `.env`: Archivo que almacena las variables de entorno necesarias para la configuración de la base de datos.

## Requisitos

- Python 3.12.3
- Paquetes instalados:
  - `pyodbc`
  - `python-dotenv`
  - `pip`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/lvildoza/python_connection_sql.git
   cd tu-repositorio
   ```

2. Instala los paquetes necesarios:
   ```bash
   pip install pyodbc python-dotenv
   ```

3. Configura tu archivo `.env` en la raíz del proyecto con las credenciales de tu base de datos:
   ```plaintext
   DB_DRIVER={el driver de tu base de datos}
   DB_SERVER={tu servidor o IP}
   DB_DATABASE={nombre de la base de datos}
   DB_USERNAME={tu nombre de usuario}
   DB_PASSWORD={tu contraseña}
   ```

## Contenido del Proyecto

### `main.py`

```python
"""
Connects to a SQL database using pyodbc
"""

from database import get_connection

def main():
    connection = get_connection()
    if connection:
        print("Conexión exitosa")

        # Crea un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecuta una consulta de ejemplo
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()

        # Cierra la conexión
        connection.close()
    else:
        print("No se pudo establecer la conexión")

if __name__ == "__main__":
    main()
```

### `database.py`

```python
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
```

### `.env`

```plaintext
DB_DRIVER={el driver de tu base de datos}
DB_SERVER={tu servidor o IP}
DB_DATABASE={nombre de la base de datos}
DB_USERNAME={tu nombre de usuario}
DB_PASSWORD={tu contraseña}
```

## Ejecución

Para ejecutar el proyecto, simplemente ejecuta `main.py`:

```bash
python main.py
```

Deberías ver un mensaje de conexión exitosa y la versión del SQL Server si todo está configurado correctamente.

## Notas

- Asegúrate de que el archivo `.env` esté en tu archivo `.gitignore` para evitar subir información sensible al repositorio.
- Verifica que los drivers y credenciales de tu base de datos sean correctos para evitar errores de conexión.